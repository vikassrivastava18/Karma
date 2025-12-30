
<template class="mx-3">
    <!-- <span v-html="iconSvg"></span> -->
    <img :src="iconSvg" alt="Icon for work type" width="20" />
</template> 

<script> 
import workIcon from './icons/work.svg';
import studyIcon from './icons/study.svg';
import prayerIcon from './icons/prayer.svg';
import playIcon from './icons/sports.svg';
import familyIcon from './icons/family.svg';
import publicIcon from './icons/people.svg';
import deletIcon from './icons/delete.svg';
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

