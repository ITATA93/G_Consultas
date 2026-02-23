# SQLUser.LBC_QCScheme

**Schema:** SQLUser
**Columnas:** 159
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCQCS_RowID | bigint | PK |  | NO | - |
| LBCQCS_Code | varchar |  |  | SI | Code |
| LBCQCS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCQCS_Comments | varchar |  |  | SI | Comments |
| LBCQCS_CreatedDate | date |  |  | SI | Created Date |
| LBCQCS_CreatedTime | time |  |  | SI | Created Time |
| LBCQCS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCQCS_DateFrom | date |  |  | SI | Date From |
| LBCQCS_DateTo | date |  |  | SI | Date To |
| LBCQCS_Desc | varchar |  |  | SI | Description |
| LBCQCS_Owner | varchar |  |  | SI | Owner |
| LBCQCS_QCResultType | varchar |  |  | NO | Quality Control Result Type |
| LBCQCS_QCSchemeType_DR | bigint |  | FK | SI | Quality Control Scheme |
| LBCQCS_RestrictToLabSites | varchar |  |  | SI | Restrict to Lab Sites |
| LBCQCS_SupplierList | varchar |  |  | SI | Supplier List (replaced LBCQCSSupplierDR) |
| LBCQCS_UpdatedDate | date |  |  | SI | Updated Date |
| LBCQCS_UpdatedTime | time |  |  | SI | Updated Time |
| LBCQCS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha de Inicio |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Informante |
| Q04 | - |  |  | SI | Procedencia |
| Q05 | - |  |  | SI | Procedencia |
| Q06 | - |  |  | SI | Anamnesis |
| Q07 | - |  |  | SI | Historia perinatal |
| Q08 | - |  |  | SI | Inmunización |
| Q09 | - |  |  | SI | Actividad física |
| Q10 | - |  |  | SI | Contacto frecuente con nivel de atención |
| Q100 | - |  |  | SI | HTML |
| Q100TxtOnly | - |  |  | SI | HTML Plain Text Only |
| Q101 | - |  |  | SI | Profesional de Salud |
| Q11 | - |  |  | SI | Condiciones familiares o sociales |
| Q12 | - |  |  | SI | Crecimiento |
| Q13 | - |  |  | SI | Pérdida reciente de peso |
| Q14 | - |  |  | SI | Desarollo |
| Q15 | - |  |  | SI | Medicamentos de uso frecuente o habitual |
| Q16 | - |  |  | SI | Notas complementarias |
| Q17 | - |  |  | SI | Estado físico general |
| Q18 | - |  |  | SI | Actitud |
| Q19 | - |  |  | SI | Disnea |
| Q20 | - |  |  | SI | Fiebre |
| Q21 | - |  |  | SI | Palidez |
| Q22 | - |  |  | SI | Ictericia |
| Q23 | - |  |  | SI | Sistema Nervioso Central |
| Q25 | - |  |  | SI | Sistema Nervioso Central |
| Q26 | - |  |  | SI | Reflejos y tono muscular normal |
| Q27 | - |  |  | SI | Ausencia de rigidez nucal |
| Q28 | - |  |  | SI | Pupilas reativas e simétricas |
| Q29 | - |  |  | SI | Fontanelas normais para a idade |
| Q30 | - |  |  | SI | Coluna vertebral sin anomalias |
| Q31 | - |  |  | SI | Circunferencia craneana nos limites normais |
| Q32 | - |  |  | SI | otrotrat |
| Q33 | - |  |  | SI | Otrotrat2 |
| Q34 | - |  |  | SI | Ojos |
| Q35 | - |  |  | SI | Ojos |
| Q36 | - |  |  | SI | Ojos de aspecto normal, bilateralmiente |
| Q37 | - |  |  | SI | Conjuntivas hiperemiadas y con exudacion |
| Q38 | - |  |  | SI | Blefaritis |
| Q39 | - |  |  | SI | ojoreser |
| Q40 | - |  |  | SI | Oido |
| Q41 | - |  |  | SI | Oido |
| Q42 | - |  |  | SI | Condutos auditivos externos y timpanos de aspecto ... |
| Q43 | - |  |  | SI | Conduto auditivo externo direito hiperemiado e ede... |
| Q44 | - |  |  | SI | Conducto auditivo externo izquierdo hiperemiado y ... |
| Q45 | - |  |  | SI | Timpano derecho abaulado y hiperemiado |
| Q46 | - |  |  | SI | Timpano derecho roto |
| Q47 | - |  |  | SI | Timpano izquierdo abaulado y hiperemiado |
| Q48 | - |  |  | SI | Timpano izquierdo roto |
| Q49 | - |  |  | SI | Secreción purulenta en el conducto auditivo derech... |
| Q50 | - |  |  | SI | Secreción purulenta en el conducto auditivo izquie... |
| Q51 | - |  |  | SI | Nariz, Boca, Pescoco |
| Q52 | - |  |  | SI | Nariz, Boca y Pescoco |
| Q53 | - |  |  | SI | Denticion esperada para a edad |
| Q54 | - |  |  | SI | Dientes en buen estado |
| Q55 | - |  |  | SI | Dientes en malo estado |
| Q56 | - |  |  | SI | Orofaringe normal |
| Q57 | - |  |  | SI | Orofaringe hiperemiada |
| Q58 | - |  |  | SI | Amígdalas hipertrofiadas y hiperemiadas |
| Q59 | - |  |  | SI | Pulmones |
| Q60 | - |  |  | SI | Pulmones |
| Q61 | - |  |  | SI | Eupneico, murmurio vesicular fisiologico |
| Q62 | - |  |  | SI | Taquipneico |
| Q63 | - |  |  | SI | Dispneico |
| Q64 | - |  |  | SI | Roncos |
| Q65 | - |  |  | SI | Sibilos expiratorios |
| Q66 | - |  |  | SI | Coracion |
| Q67 | - |  |  | SI | Coracion |
| Q68 | - |  |  | SI | Ritmo regular, en dos tiempos, sin soplos, ruidos ... |
| Q69 | - |  |  | SI | Ritmo regular en dos tiempos con soplo sistólico |
| Q70 | - |  |  | SI | Taquicardia |
| Q71 | - |  |  | SI | Abdomen |
| Q72 | - |  |  | SI | Abdomen |
| Q73 | - |  |  | SI | Abdomen depresible, sin defensa o puntos dolorosos |
| Q74 | - |  |  | SI | Ausencia de masas o viceromegalias |
| Q75 | - |  |  | SI | Genitoanal |
| Q76 | - |  |  | SI | Genitoanal |
| Q77 | - |  |  | SI | Genitalia, anus y carecteres sexuais esperados par... |
| Q78 | - |  |  | SI | Extremidades |
| Q79 | - |  |  | SI | Extremidades |
| Q80 | - |  |  | SI | Conclusión |
| Q81 | - |  |  | SI | Enfermedad de notificación obligatoria |
| Q82 | - |  |  | SI | Enfermedad con alto riesgo en contaminación comuni... |
| Q83 | - |  |  | SI | Condición cronica para el paciente, com acutizacio... |
| Q84 | - |  |  | SI | Condición aguda o nueva para el paciente |
| Q85 | - |  |  | SI | Condicion de Garantía GES |
| Q86 | - |  |  | SI | Plan |
| Q87 | - |  |  | SI | Notificar atendimiento a garantía GES |
| Q88 | - |  |  | SI | Notificar nueva garantía GES |
| Q89 | - |  |  | SI | Solicitar exámenes de laboratorio |
| Q90 | - |  |  | SI | Solicitar exámenes de imagen |
| Q91 | - |  |  | SI | Solicitar examen anatomopatológico |
| Q92 | - |  |  | SI | Periodo de observación de la evolución en la unida... |
| Q93 | - |  |  | SI | Hospitalización |
| Q94 | - |  |  | SI | Solicitar parecer especializado |
| Q95 | - |  |  | SI | Retorno programado |
| Q96 | - |  |  | SI | Exámenes laboratorio |
| Q97 | - |  |  | SI | Exámenes Imágenes |
| Q98 | - |  |  | SI | Exámenes histopatológicos |
| Q99 | - |  |  | SI | imagen |
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