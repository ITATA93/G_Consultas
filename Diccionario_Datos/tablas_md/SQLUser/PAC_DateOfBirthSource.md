# SQLUser.PAC_DateOfBirthSource

**Schema:** SQLUser
**Columnas:** 208
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOBSRC_RowId | bigint | PK |  | NO | - |
| DOBSRC_Code | varchar |  |  | NO | Code |
| DOBSRC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DOBSRC_CreatedDate | date |  |  | SI | Created Date |
| DOBSRC_CreatedTime | time |  |  | SI | Created Time |
| DOBSRC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOBSRC_DateFrom | date |  |  | SI | DateFrom |
| DOBSRC_DateTo | date |  |  | SI | DateTo |
| DOBSRC_Desc | varchar |  |  | NO | Description |
| DOBSRC_Owner | varchar |  |  | SI | Owner |
| DOBSRC_UpdatedDate | date |  |  | SI | Updated Date |
| DOBSRC_UpdatedTime | time |  |  | SI | Updated Time |
| DOBSRC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Is your gender identity the same as you were assig... |
| Q10 | - |  |  | SI | Key health questions |
| Q100 | - |  |  | SI | Liver disease or jaundice? |
| Q101 | - |  |  | SI | Do you drink alcohol? |
| Q102 | - |  |  | SI | If yes please detail number of units per week. |
| Q103 | - |  |  | SI | If yes to any of the above please detail |
| Q104 | - |  |  | SI | Genito-urinary |
| Q105 | - |  |  | SI | Do you have any kidney problems? (E.g. renal insuf... |
| Q106 | - |  |  | SI | Urinary problems including a catheter, urostomy, h... |
| Q107 | - |  |  | SI | If yes to any of the above please detail |
| Q108 | - |  |  | SI | Musculoskeletal |
| Q109 | - |  |  | SI | Do you have any muscle disease or progressive weak... |
| Q11 | - |  |  | SI | With the exception of your forthcoming surgery, ar... |
| Q110 | - |  |  | SI | Arthritis or joint problems? |
| Q111 | - |  |  | SI | If yes to any of the above please detail |
| Q112 | - |  |  | SI | Neurological |
| Q113 | - |  |  | SI | Dizziness or vertigo? |
| Q114 | - |  |  | SI | Blackouts, fainting or syncope? |
| Q115 | - |  |  | SI | Epilepsy, fits or seizures? |
| Q116 | - |  |  | SI | Any neurological problems such as multiple scleros... |
| Q117 | - |  |  | SI | Are you being treated or have you been treated for... |
| Q118 | - |  |  | SI | If yes to any of the above please detail |
| Q119 | - |  |  | SI | Cognitive function |
| Q12 | - |  |  | SI | Do you have any implants e.g shunt, orthopaedic im... |
| Q120 | - |  |  | SI | Do you have a formal diagnosis of dementia? |
| Q121 | - |  |  | SI | If yes Cognition risk assessment not required. |
| Q122 | - |  |  | SI | If no ask the following questions |
| Q123 | - |  |  | SI | Have you been more forgetful in the past 12 months... |
| Q124 | - |  |  | SI | If yes registered nurse to complete Cognition asse... |
| Q125 | - |  |  | SI | Have you attended a memory clinic? |
| Q126 | - |  |  | SI | If yes to any of the above please detail |
| Q127 | - |  |  | SI | General health |
| Q128 | - |  |  | SI | Do you have any history of anxiety, claustrophobia... |
| Q129 | - |  |  | SI | If yes please detail |
| Q13 | - |  |  | SI | Anaesthetic history |
| Q130 | - |  |  | SI | Do you have any visual or hearing impairment? |
| Q131 | - |  |  | SI | If yes, do you use any of the following |
| Q132 | - |  |  | SI | Do you have any specific individual needs, learnin... |
| Q133 | - |  |  | SI | Date of last dental check? |
| Q134 | - |  |  | SI | Do you have any body piercings? |
| Q135 | - |  |  | SI | Do you have any recent tattoos? (within the past t... |
| Q136 | - |  |  | SI | Is there a possibility you could be pregnant? |
| Q137 | - |  |  | SI | Please state the date of your last menstrual perio... |
| Q138 | - |  |  | SI | Any recent or planned prolonged travel? |
| Q139 | - |  |  | SI | Do you currently or have you previously used recre... |
| Q14 | - |  |  | SI | Have you previously had general or local anaesthet... |
| Q140 | - |  |  | SI | Is there anything in your medical history that has... |
| Q141 | - |  |  | SI | If yes to any of the above please detail |
| Q142 | - |  |  | SI | Permission to discuss treatment with next of kin? |
| Q143 | - |  |  | SI | Permission to access a summary of your medical his... |
| Q144 | - |  |  | SI | Patient consent obtained for information to be sha... |
| Q145 | - |  |  | SI | To my knowledge the above information is accurate |
| Q146 | - |  |  | SI | Patient signature area |
| Q146UDt | - |  |  | SI | Patient signature area Last Updated Date |
| Q146UTm | - |  |  | SI | Patient signature area Last Updated Time |
| Q147 | - |  |  | SI | Date |
| Q148 | - |  |  | SI | Time |
| Q149 | - |  |  | SI | Pathway |
| Q15 | - |  |  | SI | Personal or family history of any significant prob... |
| Q150 | - |  |  | SI | Date |
| Q151 | - |  |  | SI | Time |
| Q152 | - |  |  | SI | an awareness during anaesthesia, dizziness, palpit... |
| Q153 | - |  |  | SI | Any other respiratory problems such as bronchiecta... |
| Q154 | - |  |  | SI | Pulmonary Embolism (PE) (a blood clot that blocks ... |
| Q16 | - |  |  | SI | Are you able to lie flat without additional suppor... |
| Q17 | - |  |  | SI | Any back, neck, breathing problems, cramps, panic ... |
| Q18 | - |  |  | SI | Any limited movement in your back, neck or jaw, su... |
| Q19 | - |  |  | SI | Do you have any veneers, bridges, crowns, dentures... |
| Q2 | - |  |  | SI | If no please detail |
| Q20 | - |  |  | SI | Have you had a previous admission to a critical ca... |
| Q21 | - |  |  | SI | Do you have or have you had a tracheostomy? |
| Q22 | - |  |  | SI | If yes to any of the above, please detail |
| Q23 | - |  |  | SI | Cardiovascular |
| Q24 | - |  |  | SI | Key Health Questions |
| Q25 | - |  |  | SI | High blood pressure? |
| Q26 | - |  |  | SI | Atrial fibrillation, an irregular heartbeat or pal... |
| Q27 | - |  |  | SI | Pacemaker or automatic implantable cardioverter-de... |
| Q28 | - |  |  | SI | If yes, please detail the device, and the reason f... |
| Q29 | - |  |  | SI | Date when the device was last checked |
| Q3 | - |  |  | SI | What are your preferred pronouns? |
| Q30 | - |  |  | SI | Angina or pain across the front of your chest? |
| Q31 | - |  |  | SI | If yes, when do you experience angina? |
| Q32 | - |  |  | SI | Heart attack? |
| Q33 | - |  |  | SI | Heart conditions? |
| Q34 | - |  |  | SI | Percutaneous Coronary Intervention, coronary angio... |
| Q35 | - |  |  | SI | Heart failure? |
| Q36 | - |  |  | SI | Rheumatic fever, valvular disease or heart murmur? |
| Q37 | - |  |  | SI | Peripheral arterial disease (PAD) or claudication? |
| Q38 | - |  |  | SI | Stroke (cerebrovascular accident) or mini-stroke (... |
| Q39 | - |  |  | SI | Do you have any other cardiac, circulatory or vasc... |
| Q4 | - |  |  | SI | Arrangements for going home |
| Q40 | - |  |  | SI | Any family history of cardiovascular conditions? |
| Q41 | - |  |  | SI | If yes to any of the above please detail |
| Q42 | - |  |  | SI | Respiratory |
| Q43 | - |  |  | SI | Do you or have you ever smoked / vaped? |
| Q44 | - |  |  | SI | If yes |
| Q45 | - |  |  | SI | Total number of years |
| Q46 | - |  |  | SI | If yes to current smoker refer to smoking cessatio... |
| Q47 | - |  |  | SI | Breathlessness or difficulty breathing? |
| Q48 | - |  |  | SI | Are there any factors that limit your activity? |
| Q49 | - |  |  | SI | If yes, please specify |
| Q5 | - |  |  | SI | Do you have a responsible adult and suitable trans... |
| Q50 | - |  |  | SI | If other, please detail |
| Q51 | - |  |  | SI | Do you have asthma? |
| Q52 | - |  |  | SI | If yes,&nbsp |
| Q53 | - |  |  | SI | What triggers your asthma? |
| Q54 | - |  |  | SI | Do you have Chronic Obstructive Pulmonary Disease ... |
| Q55 | - |  |  | SI | Have you taken steroids in the past 3 months? |
| Q56 | - |  |  | SI | Bronchitis /  emphysema? |
| Q57 | - |  |  | SI | Pulmonary tuberculosis (TB)? |
| Q58 | - |  |  | SI | How many pillows do you sleep with under your head... |
| Q59 | - |  |  | SI | Do you have any significant lung problems or respi... |
| Q6 | - |  |  | SI | Do you have a responsible adult to stay with you o... |
| Q60 | - |  |  | SI | Do you have Obstructive Sleep Apnoea (OSA)? |
| Q61 | - |  |  | SI | If yes do you require Continuous Positive Airway P... |
| Q62 | - |  |  | SI | If yes to OSA do not complete Stopbang risk assess... |
| Q63 | - |  |  | SI | Registered nurse to complete Stopbang if BMI > 35k... |
| Q64 | - |  |  | SI | If no OSA, complete Stopbang assessment |
| Q65 | - |  |  | SI | Do you snore when you sleep? |
| Q66 | - |  |  | SI | Do you experience excessive sleepiness when awake? |
| Q67 | - |  |  | SI | Have you ever been told that you stop breathing wh... |
| Q68 | - |  |  | SI | If yes to any of the above, Registered Nurse to co... |
| Q69 | - |  |  | SI | Have you ever had Covid-19 infection? |
| Q7 | - |  |  | SI | Please tell us about your support arrangements at ... |
| Q70 | - |  |  | SI | If yes, have you been diagnosed with long Covid? |
| Q71 | - |  |  | SI | Covid vaccination status |
| Q73 | - |  |  | SI | If yes to any of the above please detail |
| Q74 | - |  |  | SI | Endocrine |
| Q75 | - |  |  | SI | Diabetes? |
| Q76 | - |  |  | SI | If yes |
| Q77 | - |  |  | SI | Have you had a previous hospital admission relatin... |
| Q78 | - |  |  | SI | Have you had your HbA1c measured within the last 3... |
| Q79 | - |  |  | SI | HbA1c result |
| Q8 | - |  |  | SI | What is your journey home time? |
| Q80 | - |  |  | SI | Thyroid, pituitary or adrenal problems? |
| Q81 | - |  |  | SI | If yes to any of the above please detail |
| Q82 | - |  |  | SI | Haematology |
| Q83 | - |  |  | SI | Personal or family history of any blood, bleeding ... |
| Q84 | - |  |  | SI | Anaemia? |
| Q85 | - |  |  | SI | Sickle cell disease or sickle cell trait? |
| Q86 | - |  |  | SI | Deep vein thrombosis (DVT) (a blood clot that deve... |
| Q87 | - |  |  | SI | Do you have a family history of Deep Vein Thrombos... |
| Q88 | - |  |  | SI | Are you taking any blood thinners? |
| Q89 | - |  |  | SI | If yes to any of the above please detail |
| Q9 | - |  |  | SI | Confirm with the patient that they must not drive ... |
| Q90 | - |  |  | SI | Gastro-intestinal |
| Q91 | - |  |  | SI | Gastric ulceration? |
| Q92 | - |  |  | SI | Gastro-oesophageal reflux disease (GORD) or heartb... |
| Q93 | - |  |  | SI | Hiatus hernia? |
| Q94 | - |  |  | SI | Are your bowel movements regular? |
| Q95 | - |  |  | SI | Do you have any bowel problems? |
| Q96 | - |  |  | SI | Colostomy or ileostomy? if yes please detail |
| Q97 | - |  |  | SI | Do you have any dietary requirements? |
| Q98 | - |  |  | SI | If yes to any of the above please detail |
| Q99 | - |  |  | SI | Hepatic |
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