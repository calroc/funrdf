
$(function() {
  $('#cake').submit(function() {
    action_url = $("#cake")[0].action;
	action_url = action_url.substr(-32);
    cmd = $("#command")[0].value;
    enact(action_url, cmd);
    return false;
  });
});

function renderState(data) {
  alert(data);
}

function enact(key, cmd){
$.post(
  "/xerblin/" + key, // 9386a06940f848eaab0d8e3b7a0dbc46"
  {command:cmd}, //"23 14 add"
  function(data, textStatus, xhr) {
    if (xhr.status == "201") {
      var next_state_url = xhr.getResponseHeader("Content-Location");
      $("form")[0].action = "/xerblin/" + next_state_url;
      renderState(data);
    }
  }, 
  'json'
  );
}
