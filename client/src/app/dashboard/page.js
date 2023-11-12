'use client'
import axios from 'axios'
import { useState, useEffect } from 'react';
import { Suspense } from 'react';
import Loading from './loading';

export const dynamic = 'force-dynamic';


const Page = ({ searchParams }) => {

    const [slow, setSlow] = useState(null)

    useEffect(() => {

        const loader = async () => {
            try {
                const config = {
                    headers: {
                        "Content-Type": "application/json",
                        'Cache-Control': 'no-cache, no-store, must-revalidate',
                        'Pragma': 'no-cache',
                        'Expires': '0',
                    },
                };

                const res = await axios.get("http://localhost:8080/api/v1/auth/get-stuff", config)

                setSlow(res.data.stuff)

            }
            catch (e) {
                console.error("Error fetching data:", e);
            }
        }
        loader()
    }, [])

    return (
        <Suspense fallback={<Loading />}>
            <h1>NAV</h1>
            <div>{slow}</div>
        </Suspense>

    )
}


export default Page