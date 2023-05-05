function getCurrentURL () {
    return window.location.href
  }

const currentUrl = getCurrentURL()


if (currentUrl.includes('analyse')) {
    document.querySelector('.navlink[href="/analyse"]').classList.add('active')
} else if (currentUrl.includes('about')) {
    document.querySelector('.navlink[href="/about"]').classList.add('active')
} else if (currentUrl.includes('contact')) {
    document.querySelector('.navlink[href="/contact"]').classList.add('active')
} else {
    document.querySelector('.navlink[href="/"]').classList.add('active')
}