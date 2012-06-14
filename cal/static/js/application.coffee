$(document).ready () ->
  calendar = $('#calendar')
  todo_form = $('#todo-form')

  public = () ->
    url = document.URL
    frag = url.split('public')
    if frag.length == 2
      frag[1] 
    else 
      "/"

  calendar.fullCalendar
    eventSources: [
      {
        url: '/todos'+public()
        type: 'GET'
        error: () ->
            alert('there was an error while fetching events!')
        color: 'yellow'
        textColor: 'black'
      }
    ]
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
    $.post "/todos/", JSON.stringify({
      start: event.start.toISOString()
      title: event.title
    }), (data) ->
      todo_form.modal 'toggle'

  $('#share').on 'click', () ->
    href = $(this).attr('href')
    $.ajax
      type: 'POST',
      url: href,
      success: () ->
        $('#unshare').show()
        $('#share-calendar').modal 'toggle'
    false
      

  $('#unshare').on 'click', () ->
    that = $(this)
    href = that.attr('href')
    $.ajax
      type: 'POST',
      url: href,
      success: () ->
        that.hide()
    false
      

