{% extends 'main.html'%}

{ % block content % }

<img style = "max-width:500px; "src = "{{ project.featured_image.url }}" >

<h1 > {{project.title}}t < /h1 >

<hr >
{ % for tag in project.tags.all % }
    <span style = "border:1px solid grey" > {{tag}} < /span >
{ % endfor % }

<hr >
<br >
<p > {{project.description}} < /p >

<main class = "singleProject my-md" >
    <div class = "container" >
      <div class = "layout" >
        <div class = "column column--1of3" >
          <h3 class = "singleProject__subtitle" > Tools & Stacks < /h3 >
          <div class = "singleProject__toolStack" >

            { % for tag in project.tags.all % }

            <span class = "tag tag--pill tag--sub tag--lg" >
              <small > {{tag}} < /small >
            </span >
            { % endfor % }
          </div >
          { % if project.source_link % }
          <a class = "singleProject__liveLink" href = "#" target = "_blank" > <i class = "im im-external-link" > </i > Source Code
          </a >
          { % endif % }
          { % if project.demo_link % }
          <a class = "singleProject__liveLink" href = "#" target = "_blank" > <i class = "im im-external-link" > </i > Live Demo
          </a >
          { % endif % }
        </div >
        <div class = "column column--2of3" >
          <img class = "singleProject__preview" src = "{{ project.featured_image.url }}" alt = "portfolio thumbnail" / >
          <a href = "profile.html" class = "singleProject__developer" > {{project.owner.name}} < /a >
          <h2 class = "singleProject__title" > {{project.title}} < /h2 >
          <h3 class = "singleProject__subtitle" > About the Project < /h3 >
          <div class = "singleProject__info" >
                {{project.description}}
          </div >

          <div class = "comments" >
            <h3 class = "singleProject__subtitle" > Feedback < /h3 >
            <h5 class = "project--rating" >
                {{project.vote_ratio}} % Postitive Feedback({{project.vote_total}} Vote{{project.vote_total | pluralize: "s"}})
            </h5 >

            <form class = "form" action = "{% url 'project' project.id %}" method = "POST" >
              { % csrf_token % }
              { % for fiedl in form % }
              <div class = "form__field" >
                <label for = "formInput#textarea" > {{field.label}} < /label >
                {{field}}
              </div >
              { % endfor % }
              <input class = "btn btn--sub btn--lg" type = "submit" value = "Add Review" / >
            </form >
            <div class = "commentList" >
              { % for review in project.review_set.all % }
              { % if review.body % }
              <div class = "comment" >
                <a href = "{% url 'user-profile' review.owner.id %}" >
                  <img class = "avatar avatar--md"
                    src = "{{review.owner.profile_image.url}}" alt = "user" / >
                </a >
                <div class = "comment__details" >
                  <a href = "{% url 'user-profile' review.owner.id %}" class = "comment__author" > {{review.owner.name}} < /a >
                  <p class = "comment__info" > {{review.body | linebreaksbr}} < /p >
                </div >
              </div >
              { % endif % }
             {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
  </main>

{% endblock content %}