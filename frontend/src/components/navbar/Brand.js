import React from 'react';
import styled from 'styled-components';

import logo from '../../assets/duemore_logo.png';

const Brand = () => {
    return (
        <Image src={logo} alt="Due More Logo" />
    )
}

export default Brand;

const Image = styled.img`
    height: 90%;
    margin: auto 0;
`;