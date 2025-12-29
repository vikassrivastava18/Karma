
<template class="mx-3">
    <!-- <span v-html="iconSvg"></span> -->
    <img :src="iconSvg" alt="Icon for work type" width="20" />
</template> 

<script> 

import workIcon from '@/assets/icons/work.svg';
import studyIcon from '@/assets/icons/study.svg';
import prayerIcon from '@/assets/icons/prayer.svg';
import playIcon from '@/assets/icons/sports.svg';
import familyIcon from '@/assets/icons/family.svg';
import publicIcon from '@/assets/icons/people.svg';
import deletIcon from '@/assets/icons/delete.svg';
// Import other icons as needed


export default {
    name: 'IconComponent',
    props: {
        type: {
            type: String,
            required: true
        }
    },
    computed: {
        iconSvg() {
            switch (this.type) {
                case 'wo':
                    return workIcon;
                case 'st':
                    return studyIcon;
                case 'pr':
                    return prayerIcon;
                case 'pl':
                    return playIcon;
                case 'ho':
                    return familyIcon;
                case 'pu':
                    return publicIcon;
                case 'ar':
                    return deletIcon;
                // Add more cases as needed
                default:
                    return '';
            }
        }
    }
}
</script>

