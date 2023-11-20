import axios from 'axios'
import { NextResponse } from 'next/server';
import { cookies } from 'next/headers'


export async function POST(request) {
    const payload = await request.json()
    // const formParams = new URLSearchParams();
    // formParams.append("client_id", process.env.NEXT_PUBLIC_CLIENT_ID)
    // formParams.append("client_secret", process.env.CLIENT_SECRET)
    // formParams.append("code", payload.code)
    // formParams.append("code_verifier", process.env.CODE_VERIFIER)
    // formParams.append("redirect_uri", process.env.NEXT_PUBLIC_REDIRECT_URI)
    // formParams.append("grant_type", "authorization_code")
    let response = ''
    const data = {
        code: payload.code,
        redirect_uri: process.env.NEXT_PUBLIC_REDIRECT_URI
    }
    try {
        // server needs to call this so that it can set cookies
        response = await axios.post('http://nginx/api/v1/auth/token/', data, { withCredentials: true })
        cookies().set({
            name: 'refresh_token',
            value: response.data.refresh_token,
            httpOnly: true,
            path: '/',
            sameSite: "Lax"
        })
    } catch (err) {
        throw new Error(err)
    }
    return Response.json(response.data)


}