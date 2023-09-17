import React from 'react';
import { GoogleOAuthProvider, GoogleLogin } from '@react-oauth/google';
import { b64utoutf8, KJUR } from 'jsrsasign';
import { useNavigate } from "react-router-dom";

const onSuccess = (credentialResponse) => {
    console.log(credentialResponse);
    // var sJWT = credentialResponse.credential;
    // var headerObj = KJUR.jws.JWS.readSafeJSONString(b64utoutf8(sJWT.split(".")[0]));
    // var payloadObj = KJUR.jws.JWS.readSafeJSONString(b64utoutf8(sJWT.split(".")[1]));
}

const Login = (setUser) => {
    const navigate = useNavigate();
    return (
        <GoogleOAuthProvider clientId="751367345812-ba8g7na7feqt60h1tfg56bv932hcil00.apps.googleusercontent.com">
            <GoogleLogin
                onSuccess={()=> {onSuccess();
                    navigate("home");}}
                onError={() => {
                    console.log('Login Failed:');
                }}
                type="icon"
                shape="circle"
            />
        </GoogleOAuthProvider>
    );
  };
    
  export default Login;