# SQLUser.OR_AnaestComplications

**Schema:** SQLUser
**Columnas:** 194
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COMP_ParRef | varchar | PK |  | NO | OR_Anaesthesia Parent Reference |
| COMP_Childsub | double |  |  | NO | Childsub |
| COMP_Complic_DR | bigint |  | FK | SI | Des Ref ORCAnaComplic |
| COMP_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Changes in cognition |
| Q02 | - |  |  | SI | Changes in memory |
| Q03 | - |  |  | SI | Changes in sensation |
| Q04 | - |  |  | SI | Problems with coordination |
| Q05 | - |  |  | SI | Fainting spells |
| Q06 | - |  |  | SI | Tremor |
| Q07 | - |  |  | SI | Headaches |
| Q08 | - |  |  | SI | Dizziness |
| Q09 | - |  |  | SI | Perception of health status? |
| Q10 | - |  |  | SI | Compliance of prescribed meds |
| Q100 | - |  |  | SI | Body image |
| Q101 | - |  |  | SI | General apparence |
| Q102 | - |  |  | SI | Fears |
| Q103 | - |  |  | SI | Anxieties |
| Q104 | - |  |  | SI | If Yes to the above information, include other sub... |
| Q105 | - |  |  | SI | Sensory deficits |
| Q106 | - |  |  | SI | Are they corrected? |
| Q107 | - |  |  | SI | Decision making is |
| Q108 | - |  |  | SI | Pain |
| Q109 | - |  |  | SI | Pain scale (0 to 10) |
| Q11 | - |  |  | SI | Special equipment |
| Q110 | - |  |  | SI | If Yes to the above information, include other sub... |
| Q111 | - |  |  | SI | Occupation |
| Q112 | - |  |  | SI | Employed |
| Q113 | - |  |  | SI | Family concerns |
| Q114 | - |  |  | SI | Siblings |
| Q115 | - |  |  | SI | How many siblings? |
| Q116 | - |  |  | SI | If Yes to the above information, include other sub... |
| Q117 | - |  |  | SI | Lesions |
| Q118 | - |  |  | SI | Discharge |
| Q119 | - |  |  | SI | Pain or masses |
| Q12 | - |  |  | SI | Other equipment |
| Q120 | - |  |  | SI | Are you currently involved in a sexual relationshi... |
| Q121 | - |  |  | SI | Do you use birth control? |
| Q122 | - |  |  | SI | Do you use protection for sexually transmitted dis... |
| Q123 | - |  |  | SI | Are you satisfied with your sexual relationship? |
| Q124 | - |  |  | SI | Do you have any problem with sexual activities? |
| Q125 | - |  |  | SI | If Yes to the above information, include other sub... |
| Q126 | - |  |  | SI | Are there any overt signs of stress? |
| Q127 | - |  |  | SI | Have you experienced any stressful or traumatic ev... |
| Q128 | - |  |  | SI | Have you or your family used any support or counse... |
| Q129 | - |  |  | SI | Group name |
| Q13 | - |  |  | SI | Risk for aspiration |
| Q130 | - |  |  | SI | Was the support group helpful? |
| Q131 | - |  |  | SI | If Yes to the above information, include other sub... |
| Q132 | - |  |  | SI | Is the patient exhibiting any signs of alterations... |
| Q133 | - |  |  | SI | Religion |
| Q134 | - |  |  | SI | Any religious restrictions to care (diet, blood tr... |
| Q135 | - |  |  | SI | Describe |
| Q136 | - |  |  | SI | Would you like to have your(pastor / priest / rabb... |
| Q137 | - |  |  | SI | Have your religious beliefs helped you to deal wit... |
| Q138 | - |  |  | SI | If Yes to the above information, include other sub... |
| Q139 | - |  |  | SI | 1. Health Perception / Health Management Pattern |
| Q14 | - |  |  | SI | Risk for infection |
| Q140 | - |  |  | SI | 2. Nutritional / MetabolicPattern |
| Q141 | - |  |  | SI | Changes in sensation |
| Q142 | - |  |  | SI | Date |
| Q143 | - |  |  | SI | Time |
| Q15 | - |  |  | SI | Risk for injury |
| Q16 | - |  |  | SI | If Yes to the above information, include other sub... |
| Q17 | - |  |  | SI | Temperature |
| Q17ObsDR | - |  |  | SI | Temperature DR |
| Q18 | - |  |  | SI | Height |
| Q18ObsDR | - |  |  | SI | Height DR |
| Q19 | - |  |  | SI | Weight |
| Q19ObsDR | - |  |  | SI | Weight DR |
| Q20 | - |  |  | SI | Change in skin color / texture |
| Q21 | - |  |  | SI | Excessive brusing |
| Q22 | - |  |  | SI | Skin lesions |
| Q23 | - |  |  | SI | Sores that do not heal |
| Q24 | - |  |  | SI | Change in mole |
| Q25 | - |  |  | SI | Pruritis |
| Q26 | - |  |  | SI | Skin |
| Q27 | - |  |  | SI | Skin turgor |
| Q28 | - |  |  | SI | Mouth membrane |
| Q29 | - |  |  | SI | Mouth lesions |
| Q30 | - |  |  | SI | Mouth color |
| Q31 | - |  |  | SI | Teeth |
| Q32 | - |  |  | SI | Dentures |
| Q33 | - |  |  | SI | Eyes membranes |
| Q34 | - |  |  | SI | Color of conjunctiva |
| Q35 | - |  |  | SI | Eyes lesions |
| Q36 | - |  |  | SI | Edemas |
| Q37 | - |  |  | SI | Abdominal girth (cm) |
| Q38 | - |  |  | SI | If Yes to the above information, include other sub... |
| Q39 | - |  |  | SI | Pain |
| Q40 | - |  |  | SI | Nausea |
| Q41 | - |  |  | SI | Diarrhea |
| Q42 | - |  |  | SI | Heartburn or Gastroesophageal Reflux Disease (GERD... |
| Q43 | - |  |  | SI | Jaundice |
| Q44 | - |  |  | SI | Change in appetite |
| Q45 | - |  |  | SI | Constipation |
| Q46 | - |  |  | SI | Flatus |
| Q47 | - |  |  | SI | Change in bowel habits |
| Q48 | - |  |  | SI | Haemorrhoids |
| Q49 | - |  |  | SI | Abdominal distension |
| Q50 | - |  |  | SI | Urinary hesitancy |
| Q51 | - |  |  | SI | Frequency |
| Q52 | - |  |  | SI | Change in stream |
| Q53 | - |  |  | SI | Pain with urination |
| Q54 | - |  |  | SI | Flank pain |
| Q55 | - |  |  | SI | Blood in Urine |
| Q56 | - |  |  | SI | Excessive urinary volume |
| Q57 | - |  |  | SI | Decreased urinary volume |
| Q58 | - |  |  | SI | If Yes to the above information, include other sub... |
| Q59 | - |  |  | SI | Pulse |
| Q59ObsDR | - |  |  | SI | Pulse DR |
| Q60 | - |  |  | SI | Respirations |
| Q60ObsDR | - |  |  | SI | Respirations DR |
| Q61 | - |  |  | SI | Systolic |
| Q61ObsDR | - |  |  | SI | Systolic DR |
| Q62 | - |  |  | SI | Diastolic |
| Q62ObsDR | - |  |  | SI | Diastolic DR |
| Q63 | - |  |  | SI | Pedal pulses |
| Q64 | - |  |  | SI | Frequent colds |
| Q65 | - |  |  | SI | Cough |
| Q66 | - |  |  | SI | shortness of breath |
| Q67 | - |  |  | SI | Wheezing |
| Q68 | - |  |  | SI | Pain with breathing |
| Q69 | - |  |  | SI | Coughing up blood |
| Q70 | - |  |  | SI | Night sweats |
| Q71 | - |  |  | SI | Chest pain |
| Q72 | - |  |  | SI | Palpitations |
| Q73 | - |  |  | SI | Dyspnea |
| Q74 | - |  |  | SI | Dyspnea during sleep |
| Q75 | - |  |  | SI | Varicose veins |
| Q76 | - |  |  | SI | Leg pain with activity |
| Q77 | - |  |  | SI | Paresthesia |
| Q78 | - |  |  | SI | Muscle pain |
| Q79 | - |  |  | SI | Weakness |
| Q80 | - |  |  | SI | Joint swelling |
| Q81 | - |  |  | SI | Joint pain |
| Q82 | - |  |  | SI | Stiffness |
| Q83 | - |  |  | SI | Limitations of range of motion |
| Q84 | - |  |  | SI | Limitations in mobility |
| Q85 | - |  |  | SI | Back pain |
| Q86 | - |  |  | SI | If Yes to the above information, include other sub... |
| Q87 | - |  |  | SI | Early waking |
| Q88 | - |  |  | SI | Insomnia |
| Q89 | - |  |  | SI | Nightmares |
| Q90 | - |  |  | SI | Nap |
| Q91 | - |  |  | SI | Feel rested |
| Q92 | - |  |  | SI | Sleep |
| Q93 | - |  |  | SI | hrs/night |
| Q94 | - |  |  | SI | sleep distractors |
| Q95 | - |  |  | SI | sleep aids |
| Q96 | - |  |  | SI | Night waking |
| Q97 | - |  |  | SI | If Yes to the above information, include other sub... |
| Q98 | - |  |  | SI | Makes eye contact |
| Q99 | - |  |  | SI | Statement of self |
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