import React from 'react';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

const CodeTabs = ({ children }) => {
  return (
    <Tabs>
      {children}
    </Tabs>
  );
};

export const CodeTabItem = ({ value, label, children }) => {
  return (
    <TabItem value={value} label={label}>
      {children}
    </TabItem>
  );
};

export default CodeTabs;
