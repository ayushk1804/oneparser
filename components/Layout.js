import Head from "next/head"
import { Navbar } from "./Navbar"
export const Layout = ({ children }) => {
    return (
        <div classname="place-items-center">
            <Head>
                <title>OneParser</title>
            </Head>
            <Navbar />
            <main>
                {children}
            </main>
        </div>
    )
}
