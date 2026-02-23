# lab.EP_VisitVoice

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISVV_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISVV_AccesionNumber | varchar |  |  | SI | Accesion Number |
| VISVV_Date | date |  |  | SI | Date of creation |
| VISVV_Desc | varchar |  |  | SI | Description |
| VISVV_Order | numeric |  |  | NO | Order number |
| VISVV_Path | varchar |  |  | SI | file path |
| VISVV_RowID | varchar |  |  | NO | - |
| VISVV_Time | time |  |  | SI | Time of creation |
| VISVV_Type | varchar |  |  | SI | Type |
| VISVV_User | varchar |  |  | SI | User created |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*