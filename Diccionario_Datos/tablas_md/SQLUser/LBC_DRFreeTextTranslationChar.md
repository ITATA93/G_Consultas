# SQLUser.LBC_DRFreeTextTranslationChar

**Schema:** SQLUser
**Columnas:** 129
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCDRFTTC_ParRef | bigint | PK |  | NO | Parent DRFreeTextTranslation DR |
| LBCDRFTTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCDRFTTC_CreatedDate | date |  |  | SI | Created Date |
| LBCDRFTTC_CreatedTime | time |  |  | SI | Created Time |
| LBCDRFTTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCDRFTTC_DateFrom | date |  |  | SI | Date From |
| LBCDRFTTC_DateTo | date |  |  | SI | Date To |
| LBCDRFTTC_FromLetter | varchar |  |  | SI | From Letter |
| LBCDRFTTC_RowID | varchar |  |  | NO | - |
| LBCDRFTTC_ToString | varchar |  |  | SI | To String |
| LBCDRFTTC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCDRFTTC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCDRFTTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nombre de la Madre |
| Q02 | - |  |  | SI | Colegio |
| Q03 | - |  |  | SI | Curso |
| Q04 | - |  |  | SI | Peso |
| Q04ObsDR | - |  |  | SI | Peso DR |
| Q05 | - |  |  | SI | Talla |
| Q05ObsDR | - |  |  | SI | Talla DR |
| Q06 | - |  |  | SI | IMC |
| Q07 | - |  |  | SI | IMC (Calculado) |
| Q08 | - |  |  | SI | Circunferencia Abdominal |
| Q08ObsDR | - |  |  | SI | Circunferencia Abdominal DR |
| Q09 | - |  |  | SI | Percentil IMC - Edad |
| Q09ObsDR | - |  |  | SI | Percentil IMC - Edad DR |
| Q10 | - |  |  | SI | Percentil Talla - Edad |
| Q10ObsDR | - |  |  | SI | Percentil Talla - Edad DR |
| Q11 | - |  |  | SI | Percentil de Circunferencia Abdominal |
| Q11ObsDR | - |  |  | SI | Percentil de Circunferencia Abdominal DR |
| Q12 | - |  |  | SI | Tanner Genitales |
| Q12ObsDR | - |  |  | SI | Tanner Genitales DR |
| Q13 | - |  |  | SI | Tanner Vello Púbico |
| Q13ObsDR | - |  |  | SI | Tanner Vello Púbico DR |
| Q14 | - |  |  | SI | 1. ¿No controla el pipí de día o de noche, aunque ... |
| Q15 | - |  |  | SI | 2. ¿Se queja de dolor frecuente al hacer pipí? |
| Q16 | - |  |  | SI | 3. ¿No controla deposiciones (caca) de día o de no... |
| Q17 | - |  |  | SI | 4. ¿Actualmente tiene parásitos (gusanos) en sus d... |
| Q18 | - |  |  | SI | 5. ¿Mancha los calzoncillos con secreción o deposi... |
| Q19 | - |  |  | SI | 6. ¿Tiene picazón anal frecuente? |
| Q20 | - |  |  | SI | 7. ¿Tiene secreción de muy mal olor en el pene, pi... |
| Q21 | - |  |  | SI | 8. ¿La piel que recubre el pene es estrecha y no p... |
| Q22 | - |  |  | SI | 9. ¿Uno o ambos testículos están ausentes en escro... |
| Q23 | - |  |  | SI | 10. ¿Tiene un aumento de volumen (hinchazón) en la... |
| Q24 | - |  |  | SI | 11. ¿Tiene olor axilar similar al de un adulto (Es... |
| Q25 | - |  |  | SI | 12. ¿Ha tenido sibilancias o silbido al pecho en e... |
| Q26 | - |  |  | SI | 13. ¿Ha tenido sibilancias o silbido al pecho dura... |
| Q27 | - |  |  | SI | 14. ¿Ronca de noche? |
| Q28 | - |  |  | SI | 15. Si ronca de noche ¿tiene pausas respiratorias?... |
| Q29 | - |  |  | SI | 16. ¿Tiene actualmente piojos en su pelo? |
| Q30 | - |  |  | SI | Alguna otra inquietud manifestada por el padre/mad... |
| Q31 | - |  |  | SI | Perímetro de Cintura |
| Q31ObsDR | - |  |  | SI | Perímetro de Cintura DR |
| Q32 | - |  |  | SI | IMC por Edad |
| Q32ObsDR | - |  |  | SI | IMC por Edad DR |
| Q33 | - |  |  | SI | Peso por Edad |
| Q33ObsDR | - |  |  | SI | Peso por Edad DR |
| Q34 | - |  |  | SI | Talla por Edad |
| Q34ObsDR | - |  |  | SI | Talla por Edad DR |
| Q35 | - |  |  | SI | Puntaje Z IMC por Edad |
| Q35ObsDR | - |  |  | SI | Puntaje Z IMC por Edad DR |
| Q36 | - |  |  | SI | Puntaje Z Peso por Edad |
| Q36ObsDR | - |  |  | SI | Puntaje Z Peso por Edad DR |
| Q37 | - |  |  | SI | Puntaje Z Talla por Edad |
| Q37ObsDR | - |  |  | SI | Puntaje Z Talla por Edad DR |
| Q38 | - |  |  | SI | Calificación Estatura |
| Q38ObsDR | - |  |  | SI | Calificación Estatura DR |
| Q39 | - |  |  | SI | Estatura Padre |
| Q39ObsDR | - |  |  | SI | Estatura Padre DR |
| Q40 | - |  |  | SI | Estatura Madre |
| Q40ObsDR | - |  |  | SI | Estatura Madre DR |
| Q41 | - |  |  | SI | Talla Diana Hombres |
| Q42 | - |  |  | SI | Talla Diana Mujeres |
| Q43 | - |  |  | SI | Diagnóstico Nutricional |
| Q43ObsDR | - |  |  | SI | Diagnóstico Nutricional DR |
| Q44 | - |  |  | SI | Obesidad Abdominal según Cirunferencia de Cintura |
| Q44ObsDR | - |  |  | SI | Obesidad Abdominal según Cirunferencia de Cintura ... |
| Q45 | - |  |  | SI | Índice Cintura/Estatura |
| Q46 | - |  |  | SI | Ingresar Información en forma manual |
| Q47 | - |  |  | SI | P.A.Sistólica |
| Q47ObsDR | - |  |  | SI | P.A.Sistólica DR |
| Q48 | - |  |  | SI | P.A. Diastólica |
| Q48ObsDR | - |  |  | SI | P.A. Diastólica DR |
| Q49 | - |  |  | SI | Percentil PAS |
| Q50 | - |  |  | SI | Percentil PAD |
| QNNA01E | - |  |  | SI | Curso [REM] |
| QPNN | - |  |  | SI | Paciente NANEAS |
| QSEN | - |  |  | SI | Usuario bajo algún programa del SENAME [REM] |
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