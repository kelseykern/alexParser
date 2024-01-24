
let filters = [
              [
               ["solid"], 
               ["restful"], 
               ["oop","object oriented"]
              ],
              [
                ["azure","aws","oop","object oriented","dependency injection"]
              ],
              [
                ["debug","troubleshoot","diagnose","improve"]
              ],
              [
                [".net"],
                ["c#"],
                ["sql"],
                ["azure"]
              ],
              [
                ["leadership", "mentorship"]
              ],
              [
                ["visual studio","visual basic","git"]
              ],
              [
                ["agile","scrum","ci/cd"]
              ],
              [
                ["design","concept"]
              ],
              [
                ["github","gitlab","bitbucket","jira","asana","trello"]
              ],
              [
                ["manage", "management", "manager"],
                ["project"]
              ]
            ];

function runFilter(){
let filters = document.getElementById("FilterBodyArea");

// build children
var children = [].slice.call(filters.getElementsByTagName('input'),0);
// build ids and classes
var ids = children.map(function(child) {
   return JSON.stringify({ id: child.id});
});

alert("Filtering for: "+ids);
}

