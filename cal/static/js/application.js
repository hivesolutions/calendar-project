(function() {

  $(document).ready(function() {
    var calendar, public, todo_form;
    calendar = $('#calendar');
    todo_form = $('#todo-form');
    public = function() {
      var frag, url;
      url = document.URL;
      frag = url.split('public');
      if (frag.length === 2) {
        return frag[1];
      } else {
        return "/";
      }
    };
    calendar.fullCalendar({
      eventSources: [
        {
          url: '/todos' + public(),
          type: 'GET',
          error: function() {
            return alert('there was an error while fetching events!');
          },
          color: 'yellow',
          textColor: 'black'
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
    $('#todo-add').on('click', function() {
      var event, title;
      event = todo_form.data('eventObject');
      event.color = 'red';
      title = $("#todo-title").val();
      event.title = title;
      calendar.fullCalendar('renderEvent', event, true);
      return $.post("/todos/", JSON.stringify({
        start: event.start.toISOString(),
        title: event.title
      }), function(data) {
        return todo_form.modal('toggle');
      });
    });
    $('#share').on('click', function() {
      var href;
      href = $(this).attr('href');
      $.ajax({
        type: 'POST',
        url: href,
        success: function() {
          $('#unshare').show();
          return $('#share-calendar').modal('toggle');
        }
      });
      return false;
    });
    return $('#unshare').on('click', function() {
      var href, that;
      that = $(this);
      href = that.attr('href');
      $.ajax({
        type: 'POST',
        url: href,
        success: function() {
          return that.hide();
        }
      });
      return false;
    });
  });

}).call(this);
