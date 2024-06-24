<script>
    import fastapi from "../lib/api";
    import Error from "../components/Error.svelte";
    import {  link, push } from 'svelte-spa-router'
    import { is_login, username } from "../lib/store"
    import moment from 'moment/min/moment-with-locales'
    moment.locale('ko')

    export let params = {};
    let question_id = params.question_id;
    let question = { answers: [] };
    let content = "";
    let error = { detail: [] };

    function get_question() {
        fastapi("get", "/api/question/detail/" + question_id, {}, (json) => {
            question = json;
        });
    }

    get_question();

    function post_answer(event) {
        event.preventDefault();
        let url = "/api/answer/create/" + question_id;
        let params = {
            content: content,
        };
        fastapi(
            "post",
            url,
            params,
            (json) => {
                content = "";
                error = { detail: [] };
                get_question();
            },
            (err_json) => {
                error = err_json;
            },
        );
    }

    function delete_answer(answer_id) {
        if(window.confirm('정말로 삭제하시겠습니까?')) {
            let url = "/api/answer/delete"
            let params = {
                answer_id: answer_id
            }
            fastapi('delete', url, params, 
                (json) => {
                    get_question()
                },
                (err_json) => {
                    error = err_json
                }
            )
        }
    }
</script>

<div class="container my-3">
<!-- 그리드적용 3 * 1 -->
    <!-- 그리드 1 -->
    <div class="row1">
        <!-- 질문 -->
        <h2 class="border-bottom py-2">{question.subject}</h2>
        <div class="card my-3">
            <div class="card-body">
                <div class="card-text" style="white-space: pre-line;">{question.content}</div>
                <div class="d-flex flex-column align-items-end">
                    
                    {#if question.modify_date }
                        <div class="badge bg-light text-dark p-2">
                            <div class="mb-2">modified at</div>
                            <div class="badge bg-light text-dark p-2 ml-auto">{question.user ? question.user.username : ""}</div>
                            <div class="badge bg-light text-dark p-2 ">{moment(question.create_date).format("YY.MM.DD a hh:mm")}</div>
                        </div>
                    {:else}
                        <div class="badge bg-light text-dark p-2">
                            <div class="mb-2">modified at</div>
                            <div class="badge bg-light text-dark p-2 ml-auto">{question.user ? question.user.username : ""}</div>
                            <div class="badge bg-light text-dark p-2 ">{moment(question.create_date).format("YY.MM.DD a hh:mm")}</div>
                        </div>
                    {/if}



                </div>
            </div>
            {#if question.user && $username === question.user.username }
            <a use:link href="/question-modify/{question.id}" 
            class="btn btn-sm btn-outline-secondary position-absolute" style="top: 10px; right: 10px;">수정</a>
            {/if}
        </div>
    </div>    
    <!-- 그리드 2 -->
    
    <div class="row2">    
        <!-- 답변 목록 -->
        <h5 class="border-bottom py-2">{question.answers.length}개의 답변이 있습니다.</h5>
        {#each question.answers as answer}
        <div class="card my-3">
            <div class="card-body position-relative">
                <div class="card-text" style="white-space: pre-line;">{answer.content}</div>
                <div class="d-flex flex-column align-items-end">
                    <div class="badge bg-light text-dark p-2 ml-auto">{question.user ? question.user.username : ""}</div>
                    <div class="badge bg-light text-dark p-2">{moment(question.create_date).format("YY.MM.DD a hh:mm")}</div>
                </div>
                {#if answer.user && $username === answer.user.username }
                    <a use:link href="/answer-modify/{answer.id}" class="btn btn-sm btn-outline-secondary position-absolute" style="top: 10px; right: 10px;">수정</a>
                    <button class="btn btn-sm btn-outline-secondary" on:click={() => delete_answer(answer.id) }>삭제</button>
                {/if}
            </div>
        </div>
    {/each}
    
    </div>    
            
    <!-- 답변 등록 -->
    <div class="row3"> 
        <div class="my-3"><Error {error} /></div>
        <form method="post">
            <div class="mb-3">
                <textarea rows="10" bind:value={content}  disabled={$is_login ? "" : "disabled"} class="form-control"></textarea>
                <div class="row align-items-center my-2">
                    <div class="col d-flex justify-content-start">
                        <button type="button" class="btn btn-secondary" on:click={() => push('/')}>목록으로</button>
                    </div>
                    <div class="col d-flex justify-content-end my-2">
                        <input type="submit" value="답변등록" class="btn btn-primary {$is_login ? '' : 'disabled'}" on:click={post_answer} />
                    </div>
                </div>
            </div>
        </form>
    </div><!-- row3 -->
</div> <!-- container -->