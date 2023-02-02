
let dummyData = { 'companies': [
    { 'name': 'TesztSoft', 'url': 'https://google.com', technologies: [ 'Go', 'C++', 'PHP'] },
    { 'name': 'MasikSoft', 'url': 'https://facebook.com', technologies: [ 'PHP', 'React'] },
]}

const container = document.getElementById('container')
const select = document.getElementById('select')
const nameInput = document.getElementById('name')
nameInput.addEventListener('input', e => { inputChange() })

function inputChange() {
    const filtered = {}
    filtered.companies = dummyData.companies.filter(comp =>
        comp.name.includes(nameInput.value))
    showData(filtered)
}

function generateOptions(data) {
    let tech = []
    data.companies.map(comp => {
        tech.push(...comp.technologies)
    })
    tech = [...new Set(tech)]
    tech.map(t => {
        const o = document.createElement('option')
        o.value = t
        o.text = t
        select.appendChild(o)
    })
}
generateOptions(dummyData)

function showData(data) {
    container.innerHTML = ''
    data.companies.map(comp => {
        const div = document.createElement('div')

        const a = document.createElement('a')
        a.innerText = comp.name
        a.href = comp.url
        a.target = '_blank'
        div.appendChild(a)

        const p = document.createElement('p')
        comp.technologies.forEach(t => {
            p.innerText += `${t} `
        })
        div.appendChild(p)

        container.appendChild(div)
    })
}
showData(dummyData)


function search() {
    const selectedTech = document.getElementById('select').value
    if(selectedTech) {
        const filtered = {}
        filtered.companies = dummyData.companies.filter(comp =>
            comp.technologies.includes(selectedTech))
        showData(filtered)
    } else {
        showData(dummyData)
    }
}
