import { type Router } from "vue-router"

export function redirect(router: Router, url: string) {
    router.push(url)
}

export function reload(router: Router) {
    router.go(0)
}