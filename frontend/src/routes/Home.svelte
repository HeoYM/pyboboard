<script>
    import fastapi from "../lib/api"
    import { link } from "svelte-spa-router"
    import { page } from "../lib/store"
    
    let question_list = []
    let size = 10;
    let total = 0;
    // svelte구문 $사용하면 종속된 변수가 변할때마다 total_page 갱신
    $: total_page = Math.ceil(total/size);


    function get_question_list(_page) {
        let params = {
            page : _page,
            size : size,
        }
        fastapi("get", "/api/question/list", params, (json) => {
            question_list = json.question_list,
            $page = _page,
            total = json.total
        });
    }

    $: get_question_list($page);
</script>

<div class="container my-3">
    
    <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>
    
    <table class="table">
        <thead>
            <tr class="table-dark">
                <th>번호</th>
                <th>제목</th>
                <th>작성일시</th>
            </tr>
        </thead>
        <tbody>
            {#each question_list as question, i}
                <tr>
                    <td>{i + 1}</td>
                    <td>
                        <a use:link href="/detail/{question.id}"
                            >{question.subject}</a
                        >
                    </td>
                    <td>{question.create_date}</td>
                </tr>
            {/each}
        </tbody>
    </table>
    
    <!-- 페이징처리 시작 -->
    <ul class="pagination pagination-sm justify-content-center">
        <!-- 이전페이지 -->
        <li class="page-item {$page <= 0 && 'disabled'}">
            <a class="page-link" href="#" aria-label="Previous" on:click="{() => get_question_list($page-1)}">
                <span aria-hidden="true">&laquo;</span>
            </a>
        </li>

    <!-- 페이지번호 -->
    {#if total_page <= 9}
        {#each Array(total_page) as _, loop_page}
            <li class="page-item {loop_page === $page && 'active'}">
                <a href="#" class="page-link" on:click="{() => get_question_list(loop_page)}">{loop_page + 1}</a>
            </li>
        {/each}
    {:else}
        {#if $page <= 5}
            {#each Array(9) as _, loop_page}
                <li class="page-item {loop_page === $page && 'active'}">
                    <a href="#" class="page-link" on:click="{() => get_question_list(loop_page)}">{loop_page + 1}</a>
                </li>
            {/each}
            <li class="page-item disabled"><span class="page-link">...</span></li>
        {:else if $page >= total_page - 4}
            <li class="page-item disabled"><span class="page-link">...</span></li>
            {#each Array(9) as _, loop_page}
                <li class="page-item {total_page - 9 + loop_page === $page && 'active'}">
                    <a href="#" class="page-link" on:click="{() => get_question_list(total_page - 9 + loop_page)}">{total_page - 9 + loop_page + 1}</a>
                </li>
            {/each}
        {:else}
            {#each Array(9) as _, loop_page}
                <li class="page-item {$page - 4 + loop_page === $page && 'active'}">
                    <a href="#" class="page-link" on:click="{() => get_question_list($page - 4 + loop_page)}">{$page - 4 + loop_page + 1}</a>
                </li>
            {/each}
            <li class="page-item disabled"><span class="page-link">...</span></li>
        {/if}
    {/if}

    <!-- 다음페이지 -->
    <li class="page-item {$page >= total_page - 1 && 'disabled'}">
        <a class="page-link" href="#" aria-label="Next" on:click="{() => get_question_list($page + 1)}">
            <span aria-hidden="true">&raquo;</span>
        </a>
    </li>
    <!-- 페이징처리 끝 -->
    
    </ul>


</div>

