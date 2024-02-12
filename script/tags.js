import grayMatterBrowser from 'https://cdn.jsdelivr.net/npm/gray-matter-browser@4.0.4/+esm'

//navbar
document.querySelector("#navMenu").addEventListener("click", () => {
    document.getElementsByClassName('navLinkGroup')[0].classList.toggle("active");
});

async function main() {
    let linksArr = [];
    await fetch("links.json")
        .then((response) => response.json())
        .then((data) => {
            linksArr = data
        });
    let tagsInfoArr = [];
    await Promise.all(
        linksArr.map(link => fetch("posts/" + link).then(res => res.text()).then(data => {
            const { metadata } = metadataParser(data);
            let tempObj = {};
            tempObj.title = metadata.title;
            tempObj.tag = metadata.categories;
            tempObj.link = link;
            tagsInfoArr.push(tempObj);
        })));

    //对象数组根据每个对象的link降序
    tagsInfoArr.sort((a, b) => {
        const linkA = a.link.toUpperCase();
        const linkB = b.link.toUpperCase();
        if (linkA < linkB) return 1;
        if (linkA > linkB) return -1;
        return 0;
    });

    let tag = "";
    tagsInfoArr.map(item => {
        if (item.tag !== tag) {
            let tagTitle = document.createElement("div");
            tagTitle.className = "tag-title";
            tagTitle.id = item.tag;
            tagTitle.textContent = item.tag;
            document.getElementsByClassName("content")[0].appendChild(tagTitle);
        }
        let tagLink = document.createElement("div");
        tagLink.className = "tag-link";
        let tagLinkA = document.createElement("a");
        tagLinkA.setAttribute("href", "posts/?title=" + item.link);
        tagLinkA.textContent = item.title;
        tagLink.appendChild(tagLinkA);
        document.getElementsByClassName("content")[0].appendChild(tagLink);
        tag = item.tag;
    })
}

function metadataParser(text) {
    const obj_md_ymal = grayMatterBrowser(text)
    return {
        metadata: obj_md_ymal.data,
        text: obj_md_ymal.content,
    };
};


main()