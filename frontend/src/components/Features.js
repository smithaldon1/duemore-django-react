import React from 'react';
import styled from 'styled-components';

const FeaturesWrapper = styled.div`
    margin-top: 7rem;
    & h1 {
        text-align: center;
    }
`;

export default function Features() {
    return (
        <FeaturesWrapper>
            <h1>Features Page</h1>
        </FeaturesWrapper>
    )
}
