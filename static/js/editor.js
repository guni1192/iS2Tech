// Vue.jsの変数展開を{{ message }}から[[ message ]]に変更する
Vue.config.delimiters = ['[[', ']]'];

window.onload = function() {
  new Vue({
    el: '#editor',
    data: {
      md_editor: '# Markdown Editor',
    },
    filters: {
      marked: marked,
    },
  });
};



