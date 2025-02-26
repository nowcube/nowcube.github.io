import grayMatterBrowser from 'https://cdn.jsdelivr.net/npm/gray-matter-browser@4.0.4/+esm'
import { marked } from "https://cdn.jsdelivr.net/npm/marked@11.2.0/lib/marked.esm.js";

//navbar
document.querySelector("#navMenu").addEventListener("click", () => {
    document.getElementsByClassName('navLinkGroup')[0].classList.toggle("active");
});


function get_card_template(title,title_href,summary,summary_href,tag,tag_herf,count,date){
    let card_template = `
        <div class="title">
            <a href="${title_href}">${title}</a>
        </div>
        <div class="summary">
            <a href="${summary_href}">${summary}</a>
        </div>
        <div class="info">
            <div class="tag">
                <a href="${tag_herf}">${tag}</a>
            </div>
            <div class="countAndDate">
                <div class="count">${count}</div>
                <div class="date">${date}</div>
            </div>
        </div>
    `;
    return card_template
}

async function main() {
    const response = await fetch('./links.json')
    const urls = await response.json()
    for (let url in urls) {
        const response = await fetch('posts/' + urls[url])
        const md_yaml = await response.text()
        //使带有ymal的md文档对象化
        const obj_md_ymal = grayMatterBrowser(md_yaml)

        // // 对文章元素命名
        const title = obj_md_ymal.data.title
        const tag = obj_md_ymal.data.categories
        const date = obj_md_ymal.data.date.toLocaleDateString()
        const md_content = marked.parse(obj_md_ymal.content)
        const pure_text = md_content.replace(/<[^>]*>/g, '')
        const count = pure_text.length+ "字"
        const summary = pure_text.substring(0, 80).concat(' ...')

        const title_href="/posts/" + "?title=" + urls[url] 
        const summary_href=title_href
        const tag_herf="./tags.html#" + tag;

        let card_div = document.createElement('div')
        card_div.setAttribute('class', 'card')
        card_div.innerHTML = get_card_template(title,title_href,summary,summary_href,tag,tag_herf,count,date)

        document.getElementsByClassName('content')[0].appendChild(card_div)
    }
}

main()


