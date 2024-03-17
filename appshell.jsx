import React, { useState } from 'react'
import { AppShell, Burger, Group, Button, Space, Title, Divider } from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';
import {IconArrowBadgeRight} from '@tabler/icons-react'; 
function AppShellTrial() {

    const [opened, { toggle }] = useDisclosure();
    const [isCreateUser, setCreateUser] = useState(false)

  function handleCreateUser(){
    alert("clicked")
    setCreateUser(true)
  }

  const createUserView = (
    <h1> In create user view page</h1>
  )

  const notcreateuser = (
    <h1> NOT ------------------? In create user view page</h1>
  )
  return (
    <AppShell
      header={{ height: 60 }}
      navbar={{ width: 300, breakpoint: 'sm', collapsed: { mobile: !opened } }}
      padding="md"
    >
      <AppShell.Header>
        <Group h="100%" px="md">
          <Burger opened={opened} onClick={toggle} hiddenFrom="sm" size="sm" />
          
        </Group>
      </AppShell.Header>
      <AppShell.Navbar >
        
        <Button variant="light" fullWidth onClick={handleCreateUser} rightSection={<IconArrowBadgeRight size={14} />}> Create User </Button>
        <Divider />
        <Button variant="light" fullWidth rightSection={<IconArrowBadgeRight size={14} />}>diptendu 2</Button>
        <Divider />
        <Button variant="light" fullWidth rightSection={<IconArrowBadgeRight size={14} />}>diptendu 3</Button>
        <Divider />
        <Button variant="light" fullWidth rightSection={<IconArrowBadgeRight size={14} />}>diptendu 4</Button>
        <Divider />
        <Button variant="light" fullWidth rightSection={<IconArrowBadgeRight size={14} />}>diptendu 5</Button>
        <Divider />
        <Button variant="light" fullWidth rightSection={<IconArrowBadgeRight size={14} />}>diptendu 6</Button>
        <Divider />
        <Button variant="light" fullWidth rightSection={<IconArrowBadgeRight size={14} />}>diptendu 7</Button>
        <Divider />
        <Button variant="light" fullWidth rightSection={<IconArrowBadgeRight size={14} />}>diptendu 8</Button>
        <Divider />
        <Button variant="light" fullWidth rightSection={<IconArrowBadgeRight size={14} />}>diptendu 9</Button>
        <Divider />
        <Button variant="light" fullWidth rightSection={<IconArrowBadgeRight size={14} />}>diptendu 10</Button>
      </AppShell.Navbar>
      <AppShell.Main>{isCreateUser ? createUserView :  notcreateuser} </AppShell.Main>
    </AppShell>
  )
}

export default AppShellTrial
