

async function slowdown() {

    const res = await fetch('http://nginx/api/v1/auth/get-stuff', {
        next: {
            revalidate: 0
        }
    })
    await new Promise(resolve => setTimeout(resolve, 3000))
    return res.json()
}

async function Page({ searchParams }) {
    const slow = await slowdown()
    console.log(searchParams.code)
    return (
        <>
            <h1>NAV</h1>
            <div>{slow.stuff}</div>
        </>

    )
}

export default Page