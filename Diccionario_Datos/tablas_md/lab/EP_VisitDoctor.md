# lab.EP_VisitDoctor

**Schema:** lab
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISDC_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISDC_Childsub | double |  |  | NO | Childsub |
| VISDC_Client_DR | varchar |  | FK | SI | Client Code DR |
| VISDC_Copies | numeric |  |  | SI | No of Copies |
| VISDC_CourierRun_DR | varchar |  | FK | SI | Courier Run |
| VISDC_DRAddress1 | varchar |  |  | SI | DR Address1 |
| VISDC_DRAddress2 | varchar |  |  | SI | DR Address2 |
| VISDC_DRAddress3_Suburb | varchar |  |  | SI | DR Suburb |
| VISDC_DRAddress4_State | varchar |  |  | SI | DR State |
| VISDC_DRAddress5_PostCode | varchar |  |  | SI | DR PostCode |
| VISDC_DoctorName | varchar |  |  | SI | Doctor Name |
| VISDC_Doctor_DR | varchar |  | FK | SI | Des Ref Doctor |
| VISDC_EDI_Type | varchar |  |  | SI | EDI Type |
| VISDC_Fax | varchar |  |  | SI | Fax |
| VISDC_FaxResult | varchar |  |  | SI | Fax Result |
| VISDC_Hospital_DR | varchar |  | FK | SI | Hospital DR |
| VISDC_Phone | varchar |  |  | SI | Phone |
| VISDC_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*