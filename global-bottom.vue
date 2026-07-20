<!-- global-bottom.vue -->
<script setup>
import { useNav, useSlideContext } from '@slidev/client'

const { currentSlideNo, total } = useNav()
const { $slidev } = useSlideContext()
</script>

<template>
    <div class="absolute bottom-0 left-0 right-0 p-2 flex items-center justify-between text-xs" style="z-index: 100;">
        <div class="flex items-center gap-2">
          <img src="/img/logo_eng.png" style="height: 20px; filter: drop-shadow(0 1px 2px rgba(0,0,0,0.45));">
          <span style="color: white; background: rgba(0,0,0,0.45); padding: 2px 8px; border-radius: 4px;">
            Faculty of Engineering, KMUTNB &middot; AI-Driven Transformation in Public Governance
          </span>
        </div>
        <div style="color: white; background: rgba(0,0,0,0.45); padding: 2px 8px; border-radius: 4px;">
          {{ $slidev.configs.module }} &middot; Page {{ currentSlideNo }} / {{ total }}
        </div>
    </div>
</template>
