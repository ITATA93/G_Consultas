# SQLUser.LB_EpisodeAction

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBEPA_ParRef | bigint | PK |  | NO | - |
| LBEPA_CloseDate | date |  |  | SI | Date of closing the action item |
| LBEPA_CloseTime | time |  |  | SI | Time of closing the action item |
| LBEPA_CloseUser_DR | bigint |  | FK | SI | Link to the user that closed the action item |
| LBEPA_Comments | varchar |  |  | SI | Free text comments |
| LBEPA_EpisodeAction_DR | bigint |  | FK | NO | Link to the code table episode action |
| LBEPA_OpenDate | date |  |  | SI | Date of opening the action item |
| LBEPA_OpenTime | time |  |  | SI | Time of opening the action item |
| LBEPA_OpenUser_DR | bigint |  | FK | SI | Link to the user that opened the action item |
| LBEPA_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | 1. Me duele el pecho o lo siento apretado |
| Q02 | - |  |  | SI | 2. Me silba el pecho o tengo ruidos al respirar |
| Q03 | - |  |  | SI | 3. Tengo ataques de asma |
| Q04 | - |  |  | SI | 4. Me asusto cuando tengo ataques de asma |
| Q05 | - |  |  | SI | 5. Me canso |
| Q06 | - |  |  | SI | 6. Tengo tos |
| Q07 | - |  |  | SI | 7. Me cuesta respirar profundo |
| Q08 | - |  |  | SI | 8. Se me tapa la nariz o me da romadizo (moco) |
| Q09 | - |  |  | SI | 9. Despierto en la noche con dificultad para respi... |
| Q10 | - |  |  | SI | 10. Me cuesta jugar con mascotas |
| Q11 | - |  |  | SI | 11. Me cuesta jugar fuera de mi casa |
| Q12 | - |  |  | SI | 1. Mis medicamentos me hacen sentir mal |
| Q13 | - |  |  | SI | 2. Mis medicamentos me dan problemas para dormir |
| Q14 | - |  |  | SI | 3. Tengo problemas para usar mi inhalador |
| Q15 | - |  |  | SI | 4. No me gusta andar con mi inhalador |
| Q16 | - |  |  | SI | 5. Me cuesta hacerme responsable de mis medicament... |
| Q17 | - |  |  | SI | 6. Es dificil para mi controlar mi asma |
| Q18 | - |  |  | SI | 7. Me niego a tomarme mis medicamentos |
| Q19 | - |  |  | SI | 8. Me olvido de usar o tomarme mis medicamentos |
| Q20 | - |  |  | SI | 9. Me asusto cuando tengo que usar mis medicamento... |
| Q21 | - |  |  | SI | 10. Me asusto cuando debo ir al médico |
| Q22 | - |  |  | SI | 11. Me asusto cuando tengo que ir a hospitalizarme |
| Q23 | - |  |  | SI | 1. Me preocupan los efectos indeseables de mis med... |
| Q24 | - |  |  | SI | 2. Me preocupo por si mi tratamiento no me está ha... |
| Q25 | - |  |  | SI | 3. Me preocupa mi asma |
| Q26 | - |  |  | SI | 1. Me cuesta decirle al médico, enfermera o kinesi... |
| Q27 | - |  |  | SI | 2. Me cuesta hacerle preguntas al médico, enfermer... |
| Q28 | - |  |  | SI | 3. Me cuesta explicarle mi enfermedad a los demas |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*