import Vue from 'vue';
import Router  from 'vue-router';
import Index from "../components/Index";
import Login from "../components/Login";
import Home from "../components/Home";
import CourseAll from "../components/CourseAll";
import CourseUnique from "../components/CourseUnique";
import CourseFree from "../components/CourseFree";
import Search from "../components/Search";
import CourseDetail from "../components/CourseDetail";
import Video from "../components/Video";
import Courseware from "../components/Courseware";
import Section from "../components/Section";
import My from "../components/My"
import Profile from "../components/personalbox/profilebox/Profile"
import Total from "../components/personalbox/Total"
import Collection from "../components/personalbox/Collection"
import Continue from "../components/personalbox/Continue"
import Finish from "../components/personalbox/FInish"
import Account from "../components/personalbox/Account"
import Note2 from "../components/Note2";
import NoteList from "../components/notebox/NoteList";
import NoteDt from "../components/notebox/NoteDt";
import NoteEdit from "../components/notebox/NoteEdit";
import NoteAdd from "../components/notebox/NoteAdd";




Vue.use(Router);
export default new Router({
  routes:[
    {
      path:'/',
      name:'index',
      component:Index,
      children:[
        {
          path:'',
          name:'home',
          component:Home
        },
        {
          path:'course_all',
          name:'course_all',
          component:CourseAll
        },
        {
          path:'course_unique',
          name:'course_unique',
          component:CourseUnique
        },
        {
          path:'course_free',
          name:'course_free',
          component:CourseFree
        },
        {
          path:'note',
          name:'note',
          component:Note2,
          beforeEnter:(to,from,next)=>{
            if (!window.localStorage.getItem('user_id')) {
              next('/login')
            }else{
              next();
            }
          },
          children:[
            {
              path:'',
              name:'note_list',
              component:NoteList
            },
            {
              path:'note_detail',
              name:'note_detail',
              component:NoteDt
            },
            {
              path:'note_edit',
              name:'note_edit',
              component:NoteEdit
            }
          ]
        },
        {
          path:'search',
          name:'search',
          component:Search
        },
        {
          path:'course_detail',
          name:'course_detail',
          component:CourseDetail
        },
        {
          path:'my/',
          name:'my',
          component:My,
          children:[
            {
              path:'profile',
              name:'profile',
              component:Profile
            },
            {
              path:'total',
              name:'total',
              component:Total
            },
            {
              path:'collection',
              name:'collection',
              component:Collection
            },
            {
              path:'continue',
              name:'continue',
              component:Continue
            },
            {
              path:'finish',
              name:'finish',
              component:Finish
            },
            {
              path:'account',
              name:'account',
              component:Account
            },
          ]
        }
      ]
    },
    {
      path:'/login',
      name:'login',
      component:Login
    },
    {
      path:'/note_add',
      name:'note_add',
      component:NoteAdd,
      beforeEnter:(to,from,next)=>{
        if (!window.localStorage.getItem('user_id')) {
          next('/login')
        }else{
          next();
        }
      },
    },
    {
      path:'/section',
      name:'section',
      component:Section,
      children: [
        {
          path:'video',
          name:'video',
          component:Video,
          beforeEnter:(to,from,next)=>{
            if (!window.localStorage.getItem('islogin')) {
              next('/login')
            }else{
              next();
            }
          }
        },
        {
          path:'courseware',
          name:'courseware',
          component:Courseware,
          beforeEnter:(to,from,next)=>{
            if (!window.localStorage.getItem('islogin')) {
              next('/login')
            }else{
              next();
            }
          }
        }
      ]
    },
  ]
});
