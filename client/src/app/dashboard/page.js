'use client'
import axios from 'axios'
import { useState, useEffect } from 'react';
import { Suspense } from 'react';
import Loading from './loading';

export const dynamic = 'force-dynamic';


const Page = ({ searchParams }) => {
    /*MAKE CODE TO PREVENT LOADING OF PAGE UNTIL ACCESS TOKEN IS IN STORAGE */
    const [data, setData] = useState([])
    useEffect(() => {


        const loader = async () => {

            try {

                const response = await axios.post("http://localhost:8080/token", { code: searchParams.code }, { withCredentials: true })
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
    }, [searchParams.code])

    return (
        <Suspense fallback={<Loading />}>
            <h1>NAV</h1>
            <div>{data.access_code}</div>
        </Suspense>

    )
}


export default Page