# SQLUser.LBC_PathogenGroupAntibioticPanel

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPAGAP_ParRef | bigint | PK |  | NO | LBCPathogenGroup Parent Reference |
| LBCPAGAP_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site DR |
| LBCPAGAP_AntibioticPanel_DR | bigint |  | FK | SI | Antibiotic Panel DR |
| LBCPAGAP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPAGAP_DateFrom | date |  |  | SI | Effective date for the record |
| LBCPAGAP_DateTo | date |  |  | SI | Last day the record is active  |
| LBCPAGAP_Default | varchar |  |  | SI | Default |
| LBCPAGAP_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCPAGAP_Lesion_DR | bigint |  | FK | SI | Lesion DR |
| LBCPAGAP_NotApplicable | varchar |  |  | SI | Not Aplicable |
| LBCPAGAP_Order | integer |  |  | SI | Order number |
| LBCPAGAP_PathogenExclusion | varchar |  |  | SI | Pathogen Exclusion
List of Pathogen IDs that are ... |
| LBCPAGAP_Pregnant | varchar |  |  | SI | Pregnant. |
| LBCPAGAP_RowID | varchar |  |  | NO | - |
| LBCPAGAP_Species_DR | bigint |  | FK | SI | Species |
| LBCPAGAP_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group DR |
| LBCPAGAP_Specimen_DR | bigint |  | FK | SI | Specimen DR |
| LBCPAGAP_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCPAGAP_WeightedSequence | double |  |  | SI | Weighted Sequence |
| Q01 | - |  |  | SI | 1.- El Adulto Mayor (AM): ¿Tiene pérdidas importan... |
| Q02 | - |  |  | SI | 2.- ¿Tiene Dificultad para expresarse de forma ver... |
| Q03 | - |  |  | SI | 3.- ¿La alteración cognitiva dificulta la realizac... |
| Q04 | - |  |  | SI | 4.- ¿Posee un Minimental abreviado bajo los 13 pun... |
| Q05 | - |  |  | SI | 5.- ¿Se ha sentido deprimido o angustiado en el úl... |
| Q06 | - |  |  | SI | 6.- El Cuidador: ¿Podrá ayudarlo(a) en actividades... |
| Q07 | - |  |  | SI | 7.- ¿Podrá acompañarlo(a) a rehabilitación 1 a 3 v... |
| Q08 | - |  |  | SI | 8.- ¿El cuidador, es una persona activa e independ... |
| Q09 | - |  |  | SI | 9.- Usted: ¿Vive con su cuidadora(or)? |
| Q10 | - |  |  | SI | 10.- ¿Posee dinero para asistir a sesiones de reha... |
| Q11 | - |  |  | SI | 11.- ¿Reside en segundos pisos (o superiores), cer... |
| Q12 | - |  |  | SI | 12.-¿Tiene sensación de perder equilibrio, inestab... |
| Q13 | - |  |  | SI | 13.- ¿Ha sufrido 2 o más caídas en los últimos 6 m... |
| Q14 | - |  |  | SI | 14.- ¿Tiene dificultad para usar bastón o andador ... |
| Q15 | - |  |  | SI | 15.- ¿ Usa usted bastones ortopédicos? |
| Q16 | - |  |  | SI | 16.- ¿ El o los bastones otopédicos o su andador s... |
| Q17 | - |  |  | SI | 17.- ¿Tiene Obesidad (IMC > a 32), HTA y/o Diabete... |
| Q18 | - |  |  | SI | 18.- ¿Sus enfermedades crónicas están en control y... |
| Q19 | - |  |  | SI | 19.- ¿Ha bajado más de 4 Kg. de peso en los último... |
| Q20 | - |  |  | SI | 20.- ¿Puede mover los brazos normalmente? |
| Q21 | - |  |  | SI | 21.- ¿Presenta dolor intenso en los brazos que dif... |
| Q22 | - |  |  | SI | 22.- Aparte de la cadera con artrosis ¿ Tiene otra... |
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