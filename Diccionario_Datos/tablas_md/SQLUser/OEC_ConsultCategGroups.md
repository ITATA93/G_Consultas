# SQLUser.OEC_ConsultCategGroups

**Schema:** SQLUser
**Columnas:** 407
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GRP_ParRef | bigint | PK |  | NO | OEC_ConsultCateg Parent Reference |
| GRP_Childsub | double |  |  | NO | Childsub |
| GRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GRP_ConsCategGroups_DR | bigint |  | FK | SI | Des Ref PACConsCategGroups |
| GRP_CreatedDate | date |  |  | SI | Created Date |
| GRP_CreatedTime | time |  |  | SI | Created Time |
| GRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GRP_DateFrom | date |  |  | SI | DateFrom  |
| GRP_DateTo | date |  |  | SI | DateTo |
| GRP_RowId | varchar |  |  | NO | - |
| GRP_UpdatedDate | date |  |  | SI | Updated Date |
| GRP_UpdatedTime | time |  |  | SI | Updated Time |
| GRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Speech |
| Q01A | - |  |  | SI | Dysphonia |
| Q01AN | - |  |  | SI | Note |
| Q01AObsDR | - |  |  | SI | Dysphonia DR |
| Q01B | - |  |  | SI | Dysarthria |
| Q01BN | - |  |  | SI | Note |
| Q01BObsDR | - |  |  | SI | Dysarthria DR |
| Q01C | - |  |  | SI | Aphasia |
| Q01CN | - |  |  | SI | Note |
| Q01CObsDR | - |  |  | SI | Aphasia DR |
| Q01D | - |  |  | SI | Other speech abnormalities |
| Q01DN | - |  |  | SI | Note |
| Q01DObsDR | - |  |  | SI | Other speech abnormalities DR |
| Q02 | - |  |  | SI | Gait |
| Q02A | - |  |  | SI | Ataxic |
| Q02AN | - |  |  | SI | Note |
| Q02AObsDR | - |  |  | SI | Ataxic DR |
| Q02B | - |  |  | SI | Shuffling |
| Q02BN | - |  |  | SI | Note |
| Q02BObsDR | - |  |  | SI | Shuffling DR |
| Q02C | - |  |  | SI | Spastic |
| Q02CN | - |  |  | SI | Note |
| Q02CObsDR | - |  |  | SI | Spastic DR |
| Q02D | - |  |  | SI | Other gait abnormalities |
| Q02DN | - |  |  | SI | Note |
| Q02DObsDR | - |  |  | SI | Other gait abnormalities DR |
| Q03 | - |  |  | SI | Memory |
| Q03A | - |  |  | SI | Impaired short term |
| Q03AN | - |  |  | SI | Note |
| Q03AObsDR | - |  |  | SI | Impaired short term DR |
| Q03B | - |  |  | SI | Impaired long term |
| Q03BN | - |  |  | SI | Note |
| Q03BObsDR | - |  |  | SI | Impaired long term DR |
| Q04 | - |  |  | SI | Orientation |
| Q04A | - |  |  | SI | Disoriented as to time |
| Q04AN | - |  |  | SI | Note |
| Q04AObsDR | - |  |  | SI | Disoriented as to time DR |
| Q04B | - |  |  | SI | Disoriented as to place |
| Q04BN | - |  |  | SI | Note |
| Q04BObsDR | - |  |  | SI | Disoriented as to place DR |
| Q04C | - |  |  | SI | Disoriented as to person |
| Q04CN | - |  |  | SI | Note |
| Q04CObsDR | - |  |  | SI | Disoriented as to person DR |
| Q05 | - |  |  | SI | Cognitive function |
| Q05A | - |  |  | SI | Impaired serial 7 calculations |
| Q05AN | - |  |  | SI | Note |
| Q05AObsDR | - |  |  | SI | Impaired serial 7 calculations DR |
| Q05B | - |  |  | SI | Impaired abstraction ability |
| Q05BN | - |  |  | SI | Note |
| Q05BObsDR | - |  |  | SI | Impaired abstraction ability DR |
| Q05C | - |  |  | SI | Impaired judgment |
| Q05CN | - |  |  | SI | Note |
| Q05CObsDR | - |  |  | SI | Impaired judgment DR |
| Q05D | - |  |  | SI | Poor general fund of information |
| Q05DN | - |  |  | SI | Note |
| Q05DObsDR | - |  |  | SI | Poor general fund of information DR |
| Q06 | - |  |  | SI | Psychological disturbances |
| Q06A | - |  |  | SI | Delusions |
| Q06AN | - |  |  | SI | Note |
| Q06AObsDR | - |  |  | SI | Delusions DR |
| Q06B | - |  |  | SI | Hallucinations |
| Q06BN | - |  |  | SI | Note |
| Q06BObsDR | - |  |  | SI | Hallucinations DR |
| Q06C | - |  |  | SI | Illusions |
| Q06CN | - |  |  | SI | Note |
| Q06CObsDR | - |  |  | SI | Illusions DR |
| Q06D | - |  |  | SI | Other psychological disturbances |
| Q06DN | - |  |  | SI | Note |
| Q06DObsDR | - |  |  | SI | Other psychological disturbances DR |
| Q07 | - |  |  | SI | Cranial nerves |
| Q07A | - |  |  | SI | Visual acuity |
| Q07AN | - |  |  | SI | Note |
| Q07AObsDR | - |  |  | SI | Visual acuity DR |
| Q07B | - |  |  | SI | Visual field deficit |
| Q07BN | - |  |  | SI | Note |
| Q07BObsDR | - |  |  | SI | Visual field deficit DR |
| Q07C | - |  |  | SI | Extraocular muscle movement |
| Q07CN | - |  |  | SI | Note |
| Q07CObsDR | - |  |  | SI | Extraocular muscle movement DR |
| Q07CRAN | - |  |  | SI | Cranial Nerves |
| Q07D | - |  |  | SI | Fundoscopy |
| Q07DN | - |  |  | SI | Note |
| Q07DObsDR | - |  |  | SI | Fundoscopy DR |
| Q07E | - |  |  | SI | Facial sensation |
| Q07EN | - |  |  | SI | Note |
| Q07EObsDR | - |  |  | SI | Facial sensation DR |
| Q07F | - |  |  | SI | Facial expression muscles |
| Q07FN | - |  |  | SI | Note |
| Q07FObsDR | - |  |  | SI | Facial expression muscles DR |
| Q07G | - |  |  | SI | Hearing |
| Q07GN | - |  |  | SI | Note |
| Q07GObsDR | - |  |  | SI | Hearing DR |
| Q07H | - |  |  | SI | Balance |
| Q07HN | - |  |  | SI | Note |
| Q07HObsDR | - |  |  | SI | Balance DR |
| Q07I | - |  |  | SI | Gag reflex |
| Q07IN | - |  |  | SI | Note |
| Q07IObsDR | - |  |  | SI | Gag reflex DR |
| Q07J | - |  |  | SI | Uvula deviation |
| Q07JN | - |  |  | SI | Note |
| Q07JObsDR | - |  |  | SI | Uvula deviation DR |
| Q07K | - |  |  | SI | Voice quality |
| Q07KN | - |  |  | SI | Note |
| Q07KObsDR | - |  |  | SI | Voice quality DR |
| Q07L | - |  |  | SI | Trapezius strength |
| Q07LN | - |  |  | SI | Note |
| Q07LObsDR | - |  |  | SI | Trapezius strength DR |
| Q08 | - |  |  | SI | Peripheral sensory system |
| Q08A | - |  |  | SI | Decreased sense of light touch |
| Q08AN | - |  |  | SI | Note |
| Q08AObsDR | - |  |  | SI | Decreased sense of light touch DR |
| Q08B | - |  |  | SI | Decreased sense of pain |
| Q08BN | - |  |  | SI | Note |
| Q08BObsDR | - |  |  | SI | Decreased sense of pain DR |
| Q08C | - |  |  | SI | Decreased sense of heat |
| Q08CN | - |  |  | SI | Note |
| Q08CObsDR | - |  |  | SI | Decreased sense of heat DR |
| Q08D | - |  |  | SI | Decreased sense of cold |
| Q08DN | - |  |  | SI | Note |
| Q08DObsDR | - |  |  | SI | Decreased sense of cold DR |
| Q08E | - |  |  | SI | Decreased sense of vibration |
| Q08EN | - |  |  | SI | Note |
| Q08EObsDR | - |  |  | SI | Decreased sense of vibration DR |
| Q08F | - |  |  | SI | Rhomberg's test |
| Q08FN | - |  |  | SI | Note |
| Q08FObsDR | - |  |  | SI | Rhomberg's test DR |
| Q09 | - |  |  | SI | Central nervous system |
| Q09A | - |  |  | SI | Abnormal joint position sense |
| Q09AN | - |  |  | SI | Note |
| Q09AObsDR | - |  |  | SI | Abnormal joint position sense DR |
| Q09B | - |  |  | SI | Impaired stereognosis |
| Q09BN | - |  |  | SI | Note |
| Q09BObsDR | - |  |  | SI | Impaired stereognosis DR |
| Q09C | - |  |  | SI | Impaired graphesthesia |
| Q09CN | - |  |  | SI | Note |
| Q09CObsDR | - |  |  | SI | Impaired graphesthesia DR |
| Q09D | - |  |  | SI | Abnormal tactile localisation |
| Q09DN | - |  |  | SI | Note |
| Q09DObsDR | - |  |  | SI | Abnormal tactile localisation DR |
| Q10 | - |  |  | SI | Muscle appearance |
| Q10A | - |  |  | SI | Muscle atrophy |
| Q10AN | - |  |  | SI | Note |
| Q10AObsDR | - |  |  | SI | Muscle atrophy DR |
| Q10B | - |  |  | SI | Muscle hypertrophy with weakness |
| Q10BN | - |  |  | SI | Note |
| Q10BObsDR | - |  |  | SI | Muscle hypertrophy with weakness DR |
| Q10C | - |  |  | SI | Resting tremor |
| Q10CN | - |  |  | SI | Note |
| Q10CObsDR | - |  |  | SI | Resting tremor DR |
| Q10D | - |  |  | SI | Choreoathetoid movements |
| Q10DN | - |  |  | SI | Note |
| Q10DObsDR | - |  |  | SI | Choreoathetoid movements DR |
| Q11 | - |  |  | SI | Muscle tone |
| Q11A | - |  |  | SI | Decreased muscle tone |
| Q11AN | - |  |  | SI | Note |
| Q11AObsDR | - |  |  | SI | Decreased muscle tone DR |
| Q11B | - |  |  | SI | General spasticity |
| Q11BN | - |  |  | SI | Note |
| Q11BObsDR | - |  |  | SI | General spasticity DR |
| Q11C | - |  |  | SI | Cogwheel (stepwise) rigidity |
| Q11CN | - |  |  | SI | Note |
| Q11CObsDR | - |  |  | SI | Cogwheel (stepwise) rigidity DR |
| Q11D | - |  |  | SI | Lead-pipe (uniform) rigidity |
| Q11DN | - |  |  | SI | Note |
| Q11DObsDR | - |  |  | SI | Lead-pipe (uniform) rigidity DR |
| Q12 | - |  |  | SI | Muscle strength |
| Q12A | - |  |  | SI | Strength grade |
| Q12AN | - |  |  | SI | Note |
| Q12AObsDR | - |  |  | SI | Strength grade DR |
| Q13 | - |  |  | SI | Involuntary movements |
| Q13A | - |  |  | SI | Fibrillations |
| Q13AN | - |  |  | SI | Note |
| Q13AObsDR | - |  |  | SI | Fibrillations DR |
| Q13B | - |  |  | SI | Fasciculations |
| Q13BN | - |  |  | SI | Note |
| Q13BObsDR | - |  |  | SI | Fasciculations DR |
| Q13C | - |  |  | SI | Tics |
| Q13CN | - |  |  | SI | Note |
| Q13CObsDR | - |  |  | SI | Tics DR |
| Q13D | - |  |  | SI | Myoclonus |
| Q13DN | - |  |  | SI | Note |
| Q13DObsDR | - |  |  | SI | Myoclonus DR |
| Q13E | - |  |  | SI | Dystonia |
| Q13EN | - |  |  | SI | Note |
| Q13EObsDR | - |  |  | SI | Dystonia DR |
| Q13F | - |  |  | SI | Chorea |
| Q13FN | - |  |  | SI | Note |
| Q13FObsDR | - |  |  | SI | Chorea DR |
| Q14 | - |  |  | SI | Reflexes |
| Q149 | - |  |  | SI | I. Olfactory |
| Q14A | - |  |  | SI | Abnormal abdominal reflex |
| Q14AN | - |  |  | SI | Note |
| Q14AObsDR | - |  |  | SI | Abnormal abdominal reflex DR |
| Q14B | - |  |  | SI | Abnormal plantar reflex |
| Q14BN | - |  |  | SI | Note |
| Q14BObsDR | - |  |  | SI | Abnormal plantar reflex DR |
| Q14C | - |  |  | SI | Abnormal deep tendon reflex |
| Q14CN | - |  |  | SI | Note |
| Q14CObsDR | - |  |  | SI | Abnormal deep tendon reflex DR |
| Q14D | - |  |  | SI | Abnormal facial reflex |
| Q14DN | - |  |  | SI | Note |
| Q14DObsDR | - |  |  | SI | Abnormal facial reflex DR |
| Q15 | - |  |  | SI | Cerebellar findings |
| Q150 | - |  |  | SI | II. Optic |
| Q151 | - |  |  | SI | III. Oculomotor |
| Q152 | - |  |  | SI | IV. Trochlear |
| Q153 | - |  |  | SI | V. Trigeminal |
| Q154 | - |  |  | SI | VI. Abducens |
| Q155 | - |  |  | SI | VII. Facial |
| Q155AA | - |  |  | SI | Motor |
| Q155AB | - |  |  | SI | Sensory-taste (2/3 tongue) |
| Q156 | - |  |  | SI | VIII. Vestibulocochlear |
| Q157 | - |  |  | SI | X. Vagus |
| Q157AA | - |  |  | SI | Gag reflex |
| Q157AB | - |  |  | SI | Phonation |
| Q157AC | - |  |  | SI | Sensory-taste (1/3 tongue) |
| Q158 | - |  |  | SI | XI. Spinal |
| Q159 | - |  |  | SI | XII. Hypoglossal |
| Q15A | - |  |  | SI | Intention tremor |
| Q15AN | - |  |  | SI | Note |
| Q15AObsDR | - |  |  | SI | Intention tremor DR |
| Q15B | - |  |  | SI | Incoordination |
| Q15BN | - |  |  | SI | Note |
| Q15BObsDR | - |  |  | SI | Incoordination DR |
| Q15C | - |  |  | SI | Dysmetria |
| Q15CN | - |  |  | SI | Note |
| Q15CObsDR | - |  |  | SI | Dysmetria DR |
| Q15D | - |  |  | SI | Dysrhythmia |
| Q15DN | - |  |  | SI | Note |
| Q15DObsDR | - |  |  | SI | Dysrhythmia DR |
| Q15E | - |  |  | SI | Dysdiadochokinesis |
| Q15EN | - |  |  | SI | Note |
| Q15EObsDR | - |  |  | SI | Dysdiadochokinesis DR |
| Q16 | - |  |  | SI | Additional notes |
| Q163 | - |  |  | SI | Ptosis |
| Q163ObsDR | - |  |  | SI | Ptosis DR |
| Q164 | - |  |  | SI | Upward movement |
| Q164ObsDR | - |  |  | SI | Upward movement DR |
| Q165 | - |  |  | SI | Downward movement |
| Q165ObsDR | - |  |  | SI | Downward movement DR |
| Q166 | - |  |  | SI | Inward movement |
| Q166ObsDR | - |  |  | SI | Inward movement DR |
| Q167 | - |  |  | SI | Vertical diplopia |
| Q167ObsDR | - |  |  | SI | Vertical diplopia DR |
| Q168 | - |  |  | SI | Hypertropia |
| Q168ObsDR | - |  |  | SI | Hypertropia DR |
| Q169 | - |  |  | SI | Facial sensitivity |
| Q169ObsDR | - |  |  | SI | Facial sensitivity DR |
| Q16TxtOnly | - |  |  | SI | Additional notes Plain Text Only |
| Q170 | - |  |  | SI | Corneal reflex |
| Q170ObsDR | - |  |  | SI | Corneal reflex DR |
| Q171 | - |  |  | SI | Motor-clench jaw |
| Q171ObsDR | - |  |  | SI | Motor-clench jaw DR |
| Q172 | - |  |  | SI | Inward deviation of eye |
| Q172ObsDR | - |  |  | SI | Inward deviation of eye DR |
| Q173 | - |  |  | SI | Inability to abduct eye |
| Q173ObsDR | - |  |  | SI | Inability to abduct eye DR |
| Q174 | - |  |  | SI | Elevate eyebrows |
| Q174ObsDR | - |  |  | SI | Elevate eyebrows DR |
| Q175 | - |  |  | SI | Close eyes tightly |
| Q175ObsDR | - |  |  | SI | Close eyes tightly DR |
| Q176 | - |  |  | SI | Show teeth |
| Q176ObsDR | - |  |  | SI | Show teeth DR |
| Q177 | - |  |  | SI | Blow out cheeks |
| Q177ObsDR | - |  |  | SI | Blow out cheeks DR |
| Q178 | - |  |  | SI | Sensory IX |
| Q178ObsDR | - |  |  | SI | Sensory IX DR |
| Q179 | - |  |  | SI | Motor X |
| Q179ObsDR | - |  |  | SI | Motor X DR |
| Q180 | - |  |  | SI | Palate |
| Q180ObsDR | - |  |  | SI | Palate DR |
| Q181 | - |  |  | SI | Swallowing |
| Q181ObsDR | - |  |  | SI | Swallowing DR |
| Q182 | - |  |  | SI | Elevate shoulder |
| Q182ObsDR | - |  |  | SI | Elevate shoulder DR |
| Q183 | - |  |  | SI | Tongue movement |
| Q183ObsDR | - |  |  | SI | Tongue movement DR |
| Q184 | - |  |  | SI | Tongue tone |
| Q184ObsDR | - |  |  | SI | Tongue tone DR |
| Q185 | - |  |  | SI | Tongue strength |
| Q185ObsDR | - |  |  | SI | Tongue strength DR |
| Q189N | - |  |  | SI | Note |
| Q190N | - |  |  | SI | Note |
| Q191N | - |  |  | SI | Note |
| Q192N | - |  |  | SI | Note |
| Q193N | - |  |  | SI | Note |
| Q194N | - |  |  | SI | Note |
| Q195N | - |  |  | SI | Note |
| Q196N | - |  |  | SI | Note |
| Q197N | - |  |  | SI | Note |
| Q198N | - |  |  | SI | Note |
| Q199N | - |  |  | SI | Note |
| Q200N | - |  |  | SI | Note |
| Q201N | - |  |  | SI | Note |
| Q202N | - |  |  | SI | Note |
| Q203N | - |  |  | SI | Note |
| Q204N | - |  |  | SI | Note |
| Q205N | - |  |  | SI | Note |
| Q206N | - |  |  | SI | Note |
| Q207N | - |  |  | SI | Note |
| Q208N | - |  |  | SI | Note |
| Q209N | - |  |  | SI | Note |
| Q210N | - |  |  | SI | Note |
| Q211N | - |  |  | SI | Note |
| Q212N | - |  |  | SI | Note |
| Q213N | - |  |  | SI | Note |
| Q214N | - |  |  | SI | Note |
| Q215N | - |  |  | SI | Note |
| Q216N | - |  |  | SI | Note |
| Q217N | - |  |  | SI | Note |
| Q218 | - |  |  | SI | Muscle power |
| Q219 | - |  |  | SI | Right upper limb |
| Q219ObsDR | - |  |  | SI | Right upper limb DR |
| Q220 | - |  |  | SI | Right lower limb |
| Q220ObsDR | - |  |  | SI | Right lower limb DR |
| Q221 | - |  |  | SI | Left upper limb |
| Q221ObsDR | - |  |  | SI | Left upper limb DR |
| Q222 | - |  |  | SI | Left lower limb |
| Q222ObsDR | - |  |  | SI | Left lower limb DR |
| Q223N | - |  |  | SI | Note |
| Q224N | - |  |  | SI | Note |
| Q227 | - |  |  | SI | Right upper limb |
| Q227A | - |  |  | SI | Biceps |
| Q227B | - |  |  | SI | Triceps |
| Q227C | - |  |  | SI | Pronator |
| Q228 | - |  |  | SI | Right lower limb |
| Q228A | - |  |  | SI | Patella |
| Q228B | - |  |  | SI | Ankle |
| Q229 | - |  |  | SI | Left upper limb |
| Q229A | - |  |  | SI | Biceps |
| Q229B | - |  |  | SI | Triceps |
| Q229C | - |  |  | SI | Pronator |
| Q230 | - |  |  | SI | Left lower limb |
| Q230A | - |  |  | SI | Patella |
| Q230B | - |  |  | SI | Ankle |
| Q231 | - |  |  | SI | Pupils |
| Q231A | - |  |  | SI | Pupil size (R) |
| Q231AN | - |  |  | SI | Note |
| Q231AObsDR | - |  |  | SI | Pupil size (R) DR |
| Q231B | - |  |  | SI | Pupil reaction (R) |
| Q231BN | - |  |  | SI | Note |
| Q231BObsDR | - |  |  | SI | Pupil reaction (R) DR |
| Q231C | - |  |  | SI | Pupil size (L) |
| Q231CN | - |  |  | SI | Note |
| Q231CObsDR | - |  |  | SI | Pupil size (L) DR |
| Q231D | - |  |  | SI | Pupil reaction (L) |
| Q231DN | - |  |  | SI | Note |
| Q231DObsDR | - |  |  | SI | Pupil reaction (L) DR |
| Q250 | - |  |  | SI | Date |
| Q251 | - |  |  | SI | Time |
| Q252 | - |  |  | SI | IX. Glossopharyngeal |
| Q253 | - |  |  | SI | Note |
| Q254 | - |  |  | SI | Uvular movement |
| Q255 | - |  |  | SI | Note |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*