(function() {

  $(document).ready(function() {
    var calendar, todo_form;
    calendar = $('#calendar');
    todo_form = $('#todo-form');
    calendar.fullCalendar({
      events: [
        {
          title: 'event1',
          start: '2012-06-13'
        }
      ],
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,agendaWeek,agendaDay'
      },
      allDayDefault: false,
      editable: false,
      droppable: false,
      eventClick: function(event, jsEvent, view) {
        if (confirm("Mark as done?")) return console.log("done");
      },
      dayClick: function(date, allDay, jsEvent, view) {
        var copy, original;
        original = $(this).data('eventObject');
        copy = $.extend({}, original);
        copy.start = date;
        copy.allDay = false;
        todo_form.data('eventObject', copy);
        return todo_form.modal('toggle');
      }
    });
    return $('#todo-add').on('click', function() {
      var event, title;
      event = todo_form.data('eventObject');
      event.color = 'red';
      title = $("#todo-title").val();
      event.title = title;
      calendar.fullCalendar('renderEvent', event, true);
      return todo_form.modal('toggle');
    });
  });

}).call(this);
