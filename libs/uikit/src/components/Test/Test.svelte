<script>
  export let rounded = false;
</script>

<button
  class={[rounded ? 'rounded-lg' : '', 'px-4', 'bg-yellow-500', 'py-2'].join(
    ' '
  )}>cool</button
>
