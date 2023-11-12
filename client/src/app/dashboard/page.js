'use client'
import axios from 'axios'
import { useState, useEffect } from 'react';
import { Suspense } from 'react';
import Loading from './loading';

export const dynamic = 'force-dynamic';


const Page = ({ searchParams }) => {

    const [data, setData] = useState([])
    useEffect(() => {


        const loader = async () => {

            try {

                const response = await axios.post("http://localhost:8080/token", { code: searchParams.code })
                setData(response.data);
                if (response.data) {
                    localStorage.setItem("access_token", JSON.stringify(response.data.access_token));
                }
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
            <div>{data.access_code}</div>
        </Suspense>

    )
}


export default Page