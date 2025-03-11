var jrvs = jrvs || {};

jrvs.subscribe = function () {
  var source = new EventSource('/events');

  source.addEventListener('message', function (message) {
    var o = JSON.parse(message.data);

    if (typeof o === 'object' && Object.keys(o.body).length > 0) {
      var el = jrvs.widgetForJob(o.job);
      o.body.updatedAt = moment().format('HH:mm');
      jrvs.render(el, {data: o.body});
    }
  }, false);
};

jrvs.widgetForJob = function (name) {
  var el = document.querySelector('[data-job="' + name + '"]');
  // If no job is specified, assume job name == widget name
  if (el === null) {
    return document.querySelector('[data-widget="' + name + '"]');
  }
  return el;
};

jrvs.render = function (widgetElement, attrs) {
  if (widgetElement === null) {
    return;
  }
  attrs = attrs || {'data': {}};
  attrs.el = widgetElement;
  m.render(widgetElement, m(window[widgetElement.dataset.widget], attrs));
};

jrvs.truncate = function (s, n) {
  if (s.length > n) {
    return s.substring(0, n) + '...';
  }
  return s;
};

jrvs.bootstrap = function() {
  if (this.readyState === XMLHttpRequest.DONE) {
    if (this.status !== 200) {
      return;
    }
    var widgets = JSON.parse(this.responseText);
    // Pre-render enabled widgets
    widgets.forEach(function (name) {
      jrvs.render(jrvs.widgetForJob(name));
    });
    // Subscribe to events
    jrvs.subscribe();
  }
};

document.addEventListener('DOMContentLoaded', function () {
  var req = new XMLHttpRequest();
  req.onreadystatechange = jrvs.bootstrap;
  req.open('GET', '/widgets');
  req.send();
});
