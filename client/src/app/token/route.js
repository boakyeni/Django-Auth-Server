import axios from 'axios'
import { NextResponse } from 'next/server';


export async function POST(request) {
    const payload = await request.json()
    const formParams = new URLSearchParams();
    formParams.append("client_id", process.env.NEXT_PUBLIC_CLIENT_ID)
    formParams.append("client_secret", process.env.CLIENT_SECRET)
    formParams.append("code", payload.code)
    formParams.append("code_verifier", process.env.CODE_VERIFIER)
    formParams.append("redirect_uri", process.env.NEXT_PUBLIC_REDIRECT_URI)
    formParams.append("grant_type", "authorization_code")
    let response = ''
    try {
        response = await axios.post('http://nginx/o/token/', formParams)
    } catch (err) {
        throw new Error("Invalid Grant", err)
    }
    return Response.json(response.data)


}