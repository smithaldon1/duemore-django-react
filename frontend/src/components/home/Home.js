import React from 'react';
import styled from 'styled-components';
import headerImg from '../../assets/do_more.png';


const Image = styled.img`
    position: relative;
    top: -7rem;
    left: 0;
    width: 100%;
`;

const HomePage = styled.div`
    margin: 2rem 0;
    & h1 {
        text-align: center;
    }
`;

const Home = () => {
    return (
        <>
            <Image src={headerImg} alt="Productive Header Image" />
            <HomePage>
                <h1>Home Page</h1>
            </HomePage>
        </>
    );
}

export default Home;