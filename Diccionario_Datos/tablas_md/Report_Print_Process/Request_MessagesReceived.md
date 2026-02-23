# Report_Print_Process.Request_MessagesReceived

**Schema:** Report_Print_Process
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente del Sistema**. Tabla interna de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| Request | bigint | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| MessagesReceived | varchar |  |  | SI | MessagesReceived |
| element_key | varchar |  |  | NO | %MessagesReceived array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*