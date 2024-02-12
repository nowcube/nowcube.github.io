import grayMatterBrowser from 'https://cdn.jsdelivr.net/npm/gray-matter-browser@4.0.4/+esm'
import { marked } from "https://cdn.jsdelivr.net/npm/marked@11.2.0/lib/marked.esm.js";

//navbar
document.querySelector("#navMenu").addEventListener("click", () => {
    document.getElementsByClassName('navLinkGroup')[0].classList.toggle("active");
});

async function main() {
    const title = getQueryVariable("title");
    const response = await fetch(title)
    const md_yaml = await response.text()
    const obj_md_ymal = grayMatterBrowser(md_yaml)
    const metadata = obj_md_ymal.data
    const md_content = marked.parse(obj_md_ymal.content)
    const pure_text = md_content.replace(/<[^>]*>/g, '')

    document.title = metadata.title + " moeday's blog";
    document.body.getElementsByClassName('title')[0].textContent = metadata.title;
    document.body.getElementsByClassName('tag')[0].querySelector("a").href = "../tags.html#" + metadata.categories;
    document.body.getElementsByClassName('tag')[0].querySelector("a").textContent = metadata.categories;
    document.body.getElementsByClassName('countAndDate')[0].textContent =pure_text.length + "字 " + metadata.date.toLocaleDateString();
    document.body.getElementsByClassName('content')[0].innerHTML = md_content;}

function getQueryVariable(variable) {
    //查询路径,如?title=2022-10-12-junior,("title")即可获取2022-10-12-junior
    const query = window.location.search.substring(1);
    const vars = query.split("&");
    for (let i = 0; i < vars.length; i++) {
        let pair = vars[i].split("=");
        if (pair[0] == variable) {
            return pair[1];
        }
    }
    return false;
}

main()