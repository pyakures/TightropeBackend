from importlib.metadata import requires
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from eventApp.models import Events
from eventApp.serializers import EventsSerializer

from eventApp.models import MindfulnessEvents
from eventApp.serializers import MindfulnessEventsSerializer

from eventApp.models import UserPreferences
from eventApp.serializers import UserPreferencesSerializer

from eventApp.models import StressSurvey
from eventApp.serializers import StressSurveySerializer

# Create your views here.
# At the moment this code will return all events, i will work on it later in order to make it return objects based on the UserID
@csrf_exempt
def eventsAPI(request,useremail=""):
    #Get all records that pertain to the useremail that is passed in the URL
    #Example: https://tightropeapi.herokuapp.com/events/test@test.com
    if request.method=='GET':
        #This is the same as:nevents = Events.objects.all().filter(UserEmail=useremail)
        events = Events.objects.filter(UserEmail=useremail)
        events_serializer = EventsSerializer(events, many=True)
        return JsonResponse(events_serializer.data,safe=False)

    #Add a record, must include all data EXCEPT for the the EventID, which is auto generated by the model
    #Example: https://tightropeapi.herokuapp.com/events/
    elif request.method=='POST':
        events_data = JSONParser().parse(request)
        events_serializer = EventsSerializer(data=events_data)
        events_serializer.is_valid()
        print(events_serializer.errors)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse("Added event!", safe=False)
        return JsonResponse("Failed to add event.", safe=False)

    #Update a record by passing a full JSON request, that includes all information for the event INCLUDING the EventID within the request
    #Example: https://tightropeapi.herokuapp.com/events/
    elif request.method=='PUT':
        events_data = JSONParser().parse(request)
        events=Events.objects.get(EventID=events_data['EventID'])
        events_serializer = EventsSerializer(events,data=events_data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse("Updated event!",safe=False)
        return JsonResponse("Failed to update event.", safe=False)
    
    #Find and delete a record by passing a full JSON request, that includes all information for the event INCLUDING the EventID within the request
    #Example: https://tightropeapi.herokuapp.com/events/
    elif request.method=='DELETE':
        events=Events.objects.get(EventID=useremail)
        events.delete()
        return JsonResponse("Deleted Sucessfully!",safe=False)
    


@csrf_exempt
def mindfulnesseventsAPI(request):
    #Get the record that pertains to the minfulness event name
    #Example: 
    if request.method=='GET':
        mindfulness_events = MindfulnessEvents.objects.all()
        serialized_mindfulness_events = MindfulnessEventsSerializer(mindfulness_events, many=True)
        return JsonResponse(serialized_mindfulness_events.data,safe=False)

    #Add a record, must include all data EXCEPT for the the MindfulnessEventID, which is auto generated by the model
    #Example: 
    elif request.method=='POST':
        new_data = JSONParser().parse(request)
        serialized_mindfulness_events = MindfulnessEventsSerializer(data=new_data)
        serialized_mindfulness_events.is_valid()
        print(serialized_mindfulness_events.errors)
        if serialized_mindfulness_events.is_valid():
            serialized_mindfulness_events.save()
            return JsonResponse("Added new Mindfulness Event!", safe=False)
        return JsonResponse("Failed to add event.", safe=False)

    #Update a record by passing a full JSON request, that includes all information for the event INCLUDING the MindfulnessEventID within the request
    #Example: 
    elif request.method=='PUT':
        events_data = JSONParser().parse(request)
        events=MindfulnessEvents.objects.get(MindfulnessEventID=events_data['MindfulnessEventID'])
        events_serializer = MindfulnessEventsSerializer(events,data=events_data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse("Updated event!",safe=False)
        return JsonResponse("Failed to update event.", safe=False)
    
    #Find and delete a record by passing a full JSON request, that includes all information for the event INCLUDING the MindfulnessEventID within the request
    #Example: 
    elif request.method=='DELETE':
        events_data = JSONParser().parse(request)
        event=MindfulnessEvents.objects.get(MindfulnessEventID=events_data['MindfulnessEventID'])
        event.delete()
        return JsonResponse("Deleted Sucessfully!",safe=False)
  


@csrf_exempt
def userMindfulnessPreferences(request, useremail=""):
    #Get a given user's mindfulness preferences
    if request.method=='GET':
        userpreferences = UserPreferences.objects.filter(UserEmail=useremail)
        serialized_preferences = UserPreferencesSerializer(userpreferences, many=True)
        return JsonResponse(serialized_preferences.data,safe=False)

    #Takes a single request for a user's preferences and adds it to database
    if request.method=='POST':
        print(request)
        user_preferences = JSONParser().parse(request)
        list = user_preferences['mindfulPreferenceIDs']
        for i in list:
            query_base_event=MindfulnessEvents.objects.filter(MindfulnessEventID=i)
            user_preference_dictionary = {}
            for base_event in query_base_event:
                user_preference_dictionary = {
                    'UserEmail': useremail,
                    'UserPreference': base_event.MindfulnessEventName,
                    'UserPreferenceDuration': base_event.MindfulnessEventDuration,
                    'UserPreferenceNotes': base_event.MindfulnessEventNotes
                }
            serialized_preferences = UserPreferencesSerializer(data=user_preference_dictionary)
            serialized_preferences.is_valid()
            print(serialized_preferences.errors)
            if serialized_preferences.is_valid():
                serialized_preferences.save()
            else:
                return JsonResponse("Failed to add event", safe=False)
        return JsonResponse("Successfully Added Preferences", safe=False)

    #I don't think this is relevant, this could be used to update a record of the user's preferences, but its standard
    if request.method=='PUT':
        pass

    #Deletes a record of a user's preferences
    #To me, this looks like it wouldn't work, might have to reqork this later
    if request.method=='DELETE':
        deletion = JSONParser().parse(request)
        event=UserPreferences.objects.get(UserPreferenceID=deletion['UserPreferenceID'])
        event.delete()
        return JsonResponse("Deleted Sucessfully!",safe=False)


@csrf_exempt
def surveyApp(request, useremail=""):
    if request.method=='GET':
        result = StressSurvey.objects.filter(UserEmail=useremail)
        serialized_survey = StressSurveySerializer(result, many=True)
        return JsonResponse(serialized_survey.data,safe=False)
    
    if request.method=='POST':
        survey_results = JSONParser().parse(request)
        serialized_survey_results = StressSurveySerializer(data=survey_results)
        serialized_survey_results.is_valid()
        print(serialized_survey_results.errors)
        if serialized_survey_results.is_valid():
            serialized_survey_results.save()
            return JsonResponse("Added new Stress Survey Result!", safe=False)
        return JsonResponse("Failed to add new result.", safe=False)
    
    if request.method=='PUT':
        new_value = JSONParser().parse(request)
        old_value=StressSurvey.objects.get(UserEmail=useremail)
        events_serializer = StressSurveySerializer(old_value, data=new_value)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse("Updated stress value!",safe=False)
        return JsonResponse("Failed to update stress value.", safe=False)
    
    if request.method=='DELETE':
        event=StressSurvey.objects.get(UserEmail=useremail)
        event.delete()
        return JsonResponse("Deleted Sucessfully!",safe=False)