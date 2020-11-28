import React from 'react';
import styled from 'styled-components';

const PricingWrapper = styled.div`
    margin-top: 7rem;
    & h1 {
        text-align: center;
    }
`;

export default function Pricing() {
    return (
        <PricingWrapper>
            <h1>Pricing Page</h1>
        </PricingWrapper>
    )
}
