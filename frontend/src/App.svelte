<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"
  import QuestionCreate from './routes/QuestionCreate.svelte';
  import Navigation from './components/Navigation.svelte';
  import UserCreate from "./routes/UserCreate.svelte"
  import UserLogin from './routes/UserLogin.svelte';
  import QuestionModify from "./routes/QuestionModify.svelte"
  import AnswerModify from "./routes/AnswerModify.svelte"

  const routes = {
    '/' : Home,
    '/question-create' : QuestionCreate,
    '/detail/:question_id' : Detail,
    '/user-create': UserCreate,
    '/user-login': UserLogin,
    '/question-modify/:question_id': QuestionModify,
    '/answer-modify/:answer_id': AnswerModify,
  }

</script>


<Navigation />
<Router {routes}/>