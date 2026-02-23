# lab.EP_VisitReporting

**Schema:** lab
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISRP_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISRP_Address1 | varchar |  |  | SI | Address1 |
| VISRP_Address2 | varchar |  |  | SI | Address2 |
| VISRP_Address3_Suburb | varchar |  |  | SI | Suburb |
| VISRP_Address4_State | varchar |  |  | SI | State |
| VISRP_Address5_PostCode | varchar |  |  | SI | PostCode |
| VISRP_Childsub | double |  |  | NO | Childsub |
| VISRP_Client_DR | varchar |  | FK | SI | Client Code DR |
| VISRP_Copies | numeric |  |  | SI | No of Copies |
| VISRP_CourierRun_DR | varchar |  | FK | SI | Courier Run |
| VISRP_Doctor_DR | varchar |  | FK | SI | Doctor DR |
| VISRP_EDIEnabled | varchar |  |  | SI | EDI Enabled |
| VISRP_EDI_Type | varchar |  |  | SI | EDI Type |
| VISRP_Fax | varchar |  |  | SI | Fax |
| VISRP_FaxCopies | numeric |  |  | SI | No of Fax Copies |
| VISRP_FaxEnabled | varchar |  |  | SI | Fax Enabled |
| VISRP_FaxFF | varchar |  |  | SI | Fax Full Final Only |
| VISRP_Hospital_DR | varchar |  | FK | SI | Hospital DR |
| VISRP_Phone1 | varchar |  |  | SI | Phone1 |
| VISRP_Phone2 | varchar |  |  | SI | Phone2 |
| VISRP_Phone3SMS | varchar |  |  | SI | Phone3SMS |
| VISRP_Phone4 | varchar |  |  | SI | Phone4 |
| VISRP_Phone5 | varchar |  |  | SI | Phone5 |
| VISRP_Phone6 | varchar |  |  | SI | Phone6 |
| VISRP_PrintEnabled | varchar |  |  | SI | Print Enabled |
| VISRP_ReportToName | varchar |  |  | SI | Report To Name |
| VISRP_RowID | varchar |  |  | NO | - |
| VISRP_SMSEnabled | varchar |  |  | SI | SMS Enabled |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*