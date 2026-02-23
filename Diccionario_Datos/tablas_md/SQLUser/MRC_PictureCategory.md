# SQLUser.MRC_PictureCategory

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PICTCAT_RowId | bigint | PK |  | NO | - |
| PICTCAT_Code | varchar |  |  | NO | Code |
| PICTCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PICTCAT_CreatedDate | date |  |  | SI | Created Date |
| PICTCAT_CreatedTime | time |  |  | SI | Created Time |
| PICTCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PICTCAT_DateFrom | date |  |  | SI | Date From |
| PICTCAT_DateTo | date |  |  | SI | Date To |
| PICTCAT_Desc | varchar |  |  | NO | Description |
| PICTCAT_Owner | varchar |  |  | SI | Owner |
| PICTCAT_UpdatedDate | date |  |  | SI | Updated Date |
| PICTCAT_UpdatedTime | time |  |  | SI | Updated Time |
| PICTCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Medicamentos al alcance de los niños |
| Q02 | - |  |  | SI | Detergentes, veneno, cloro al alcance de los niños |
| Q03 | - |  |  | SI | Materiales de construcción al alcance de los niños |
| Q04 | - |  |  | SI | Basureros al alcance de los niños |
| Q05 | - |  |  | SI | Calefón sin tubo extractor |
| Q06 | - |  |  | SI | Estufas, braseros en ambientes no ventilados |
| Q07 | - |  |  | SI | Bolsas plásticas al alcance de los niños |
| Q08 | - |  |  | SI | Plantas dentro del hogar |
| Q09 | - |  |  | SI | Conexiones de gas al alcance de los niños |
| Q10 | - |  |  | SI | Productos tóxicos en botellas de bebidas |
| Q11 | - |  |  | SI | Escaleras sin protección (puertas de seguridad) |
| Q12 | - |  |  | SI | Puertas divisorias de vidrio sin señalización |
| Q13 | - |  |  | SI | Balcones sin protección (sin mallas de segurdad) |
| Q14 | - |  |  | SI | Ventanas sin protección (sin mallas de seguridad) |
| Q15 | - |  |  | SI | Muebles cerca de las ventanas |
| Q16 | - |  |  | SI | Mesas bajas con esquinas punteagudas |
| Q17 | - |  |  | SI | Puertas batientes |
| Q18 | - |  |  | SI | Materiales de costura al alcance de los niños |
| Q19 | - |  |  | SI | Utensilios de cocina al alcance de los niños |
| Q20 | - |  |  | SI | Pisos resbaladizos al limpiarlos (tener precaución... |
| Q21 | - |  |  | SI | Alfombras no adheridas al suelo o sueltas |
| Q22 | - |  |  | SI | Rejas con barrotes de separación suficiente, para ... |
| Q23 | - |  |  | SI | Mangos de ollas hacia fuera mientras se cocina |
| Q24 | - |  |  | SI | Enchufes sin protección |
| Q25 | - |  |  | SI | Conexiones eléctricas defectuosas |
| Q26 | - |  |  | SI | Libre entrada a la cocina en hora de preparación d... |
| Q27 | - |  |  | SI | Fósforos al alcance de los niños |
| Q28 | - |  |  | SI | Chimeneas sin protección |
| Q29 | - |  |  | SI | Estufas, braseros o anafres en pasillos o sitio de... |
| Q30 | - |  |  | SI | Planchas enchufadas al alcance de lo sniños |
| Q31 | - |  |  | SI | Mesa con manteles largos |
| Q32 | - |  |  | SI | Juguetes de los hermanos mayores con partes pequeñ... |
| Q33 | - |  |  | SI | Objetos afilados como prendedores, aros, alfileres... |
| Q34 | - |  |  | SI | Armas de fuego al alcance de los niños |
| Q35 | - |  |  | SI | Puertas con seguro interno (se podrían encerrar co... |
| Q36 | - |  |  | SI | Acequias o canales cerca de la casa sin protección |
| Q37 | - |  |  | SI | Piscinas sin protección |
| Q38 | - |  |  | SI | Muebles móviles especialmente aquellos con objetos... |
| Q39 | - |  |  | SI | Cocina no fijada a la pared |
| Q40 | - |  |  | SI | Hervidores eléctricos con cable al alcance del niñ... |
| Q41 | - |  |  | SI | Transporte del niño o niña en vehículo sin  silla ... |
| Q42 | - |  |  | SI | Hemos tomado las siguientes medidas frente a los p... |
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