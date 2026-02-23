# questionnaire.QTCEROPRORE

> Rehabilitación Oral: Protesis Removible

**Schema:** questionnaire
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Rehabilitación Oral: Protesis Removible

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Diagnóstico |
| Q02 | varchar |  |  | SI | Diagnóstico Maxilar Superior |
| Q03 | varchar |  |  | SI | Diagnóstico Maxilar Inferioir |
| Q04 | varchar |  |  | SI | Observaciones |
| Q05 | varchar |  |  | SI | Kennedy Maxilar Superior |
| Q06 | varchar |  |  | SI | Kennedy Maxilar Inferior |
| Q08 | date |  |  | SI | Fecha |
| Q09 | date |  |  | SI | Impresion Preliminar |
| Q10 | date |  |  | SI | Impresion Definitiva |
| Q11 | date |  |  | SI | Cubeta |
| Q12 | date |  |  | SI | Altura y/o Prueba de Base + Prueba de Color |
| Q13 | date |  |  | SI | Prueba de Cera |
| Q14 | date |  |  | SI | Instalación/Alta |
| Q15 | varchar |  |  | SI | Entrego Protesis y Cito a Control |
| Q16 | bit |  |  | SI | Acta de Recepción |
| Q17 | bit |  |  | SI | Comprobante de Recepción de Protesis |
| Q18 | varchar |  |  | SI | Controles |
| Q19 | varchar |  |  | SI | Pronostico |
| Q20 | bit |  |  | SI | Superior 1 |
| Q21 | bit |  |  | SI | Superior Parcial Acrílica |
| Q22 | bit |  |  | SI | Superior Total Acrílica |
| Q23 | bit |  |  | SI | Inferior1 |
| Q24 | bit |  |  | SI | Inferior Parcial Acrílica |
| Q25 | bit |  |  | SI | Inferior Total Acrílica |
| Q26 | varchar |  |  | SI | Color |
| Q28 | varchar |  |  | SI | Desea Agregar Nuevo Tratamiento [1] |
| Q29 | varchar |  |  | SI | Desea Agregar Nuevo Tratamiento [2] |
| Q30 | varchar |  |  | SI | Desea Agregar Nuevo Tratamiento [3] |
| Q31 | date |  |  | SI | Impresion Preliminar 1 |
| Q32 | date |  |  | SI | Impresion Preliminar 2 |
| Q33 | date |  |  | SI | Impresion Preliminar 3 |
| Q34 | date |  |  | SI | Impresion Definitiva 1 |
| Q35b | date |  |  | SI | Impresion Definitiva 2 |
| Q36 | date |  |  | SI | Impresion Definitiva 3 |
| Q36b | date |  |  | SI | Cubeta 1 |
| Q37 | date |  |  | SI | Cubeta 2 |
| Q38 | date |  |  | SI | Cubeta 3 |
| Q39 | date |  |  | SI | Altura y/o Prueba de Base + Prueba de Color 1 |
| Q40 | date |  |  | SI | Altura y/o Prueba de Base + Prueba de Color 2 |
| Q41 | date |  |  | SI | Altura y/o Prueba de Base + Prueba de Color 3 |
| Q42 | date |  |  | SI | Prueba de cera 1 |
| Q43 | date |  |  | SI | prueba de cera 2 |
| Q44 | date |  |  | SI | prueba de cera 3 |
| Q45b | date |  |  | SI | Instalacion Alta 1 |
| Q46 | date |  |  | SI | Instalacion? Alta 2 |
| Q47 | date |  |  | SI | Instalacion Alta 3 |
| Q49 | varchar |  |  | SI | Tratamiento |
| Q50 | date |  |  | SI | Fecha Control |
| Q51 | varchar |  |  | SI | Comentario |
| Q52 | varchar |  |  | SI | Contenido 2  |
| Q54 | varchar |  |  | SI | Color 1 |
| Q55 | varchar |  |  | SI | Color 2 |
| Q56 | varchar |  |  | SI | Color 3 |
| Q57 | varchar |  |  | SI | Color 4 |
| Q59 | varchar |  |  | SI | Digitado Por |
| Q60 | varchar |  |  | SI | Cera |
| Q61 | varchar |  |  | SI | Cera 1 |
| Q62 | varchar |  |  | SI | Cera 2 |
| Q63 | varchar |  |  | SI | Cera 3 |
| Q66 | varchar |  |  | SI | Pronóstico Observación |
| QRem1 | date |  |  | SI | Instalación/Alta |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*