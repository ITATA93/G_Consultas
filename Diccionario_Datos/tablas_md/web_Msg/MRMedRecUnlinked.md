# web_Msg.MRMedRecUnlinked

**Schema:** web_Msg
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| MRMedicationDR | varchar |  | FK | SI | Des Ref MRMedication |
| OEOrdItemDR | varchar |  | FK | SI | Des Ref OEOrdItem |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |
| webMsgParRef | varchar |  |  | SI | ParRef |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*