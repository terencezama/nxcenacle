<script>
  import { Meta, Story, Template } from '@storybook/addon-svelte-csf';

  import Test from './Test.svelte';

  let count = 0;
  function handleClick() {
    count += 1;
  }
</script>

<Meta title="Test" component={Test} />

<Template let:args>
  <Test {...args} on:click={handleClick}>
    You clicked: {count}
  </Test>
</Template>

<Story name="Rounded" args={{ rounded: true }} />

<Story name="Square" source args={{ rounded: false }} />

<!-- Dynamic snippet should be disabled for this story -->
<Story name="Button No Args">
  <Test>Label</Test>
</Story>
