<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"
  import QuestionCreate from './routes/QuestionCreate.svelte';

  const routes = {
    '/' : Home,
    '/question-create' : QuestionCreate,
    '/detail/:question_id' : Detail,
    
  }
</script>

<Router {routes}/>