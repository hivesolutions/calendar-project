$(document).ready () ->
  calendar = $('#calendar')
  todo_form = $('#todo-form')

  calendar.fullCalendar
    events: [{
            title  : 'event1',
            start  : '2012-06-13'
        }]
    header:
        left: 'prev,next today'
        center: 'title'
        right: 'month,agendaWeek,agendaDay'
    allDayDefault: false
    editable: false
    droppable: false
    eventClick: (event, jsEvent, view) ->
      if confirm("Mark as done?")
        console.log "done"
    dayClick: (date, allDay, jsEvent, view) ->
      original = $(this).data 'eventObject'
      copy = $.extend {}, original
      copy.start = date
      copy.allDay = false
      todo_form.data 'eventObject', copy
      todo_form.modal 'toggle'

  $('#todo-add').on 'click', () ->
    event = todo_form.data 'eventObject'
    event.color = 'red'
    title = $("#todo-title").val()
    event.title = title
    calendar.fullCalendar 'renderEvent', event, true
    todo_form.modal 'toggle'

